
from sanic.blueprints import Blueprint
from sanic.response import json

from models.message import Message 
from sanic_openapi import doc

from utils import id_generator, checks, hashing

# Create the main blueprint to work with
blueprint = Blueprint('User_API', url_prefix="/user")

import time

@blueprint.get("/<thread_id:int>", strict_slashes=True)
@doc.summary("Fetches user information.")
def user_get(request, thread_id):
    db = request.ctx.db
    channel_or_user = thread_id # For readability 

    data = db.query_row("SELECT id, _name FROM users WHERE id = ?" , thread_id)
    if not data:
        return json({"op": "void"}, status=404)
    return json(data, status=200)


@blueprint.post("/create", strict_slashes=True)
@doc.summary("Create a user.")
def user_create(request):
    db = request.ctx.db

    data = request.json
    _id = id_generator.generate_user_id(db)

    password_obj = request.ctx.hasher.hash_password(request.json['auth']) 

    db.execute("INSERT INTO users (id, _name, authentication, salt, created_at) VALUES (?,?,?,?,?)" , _id, data["username"], password_obj.hash, password_obj.salt, time.time())
    return json({"op": "created.", "id": _id}, status=200)


@blueprint.delete("/<thread_id:int>/delete", strict_slashes=True)
@doc.summary("Deletes a user.")
def user_delete(request, thread_id):
    db = request.ctx.db
    user = thread_id # For readability 

    if not checks.authenticated(request.json["auth"], id_generator.generate_session_token(request.ctx.redis, user)):
        return json({"op": "unauthorized."}, status=401)

    db.execute("DELETE FROM users WHERE id = ?", user)
    return json({"op": "deleted"}, status=200)


@blueprint.post("/<thread_id:int>/authkey", strict_slashes=True)
@doc.summary("Generate an auth key for a user.") # Aka logging in.
def user_authkey(request, thread_id):
    db = request.ctx.db
    user = thread_id # For readability 

    data = db.query_row("SELECT authentication, salt, created_at FROM users WHERE id = ?" , user)
    if not data:
        return json({"op": "void"}, status=404) # it doesnt exist
    _json = request.json
    check = request.ctx.hasher.verify_password_hash(_json['auth'], data['authentication'], data['salt']) # Verify their password is correct.

    if check != True: # the hash doesnt match
        return json({"op": "void"}, status=404)
    
    elif check == True: # the hash matches
        key = id_generator.generate_session_token(request.ctx.redis, user)
        return json({"op": "created", "authentication": key})
