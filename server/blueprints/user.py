
from sanic.blueprints import Blueprint
from sanic.response import json

from models.message import Message 
from sanic_openapi import doc

# Create the main blueprint to work with
blueprint = Blueprint('User_API', url_prefix="/user")

import random

@blueprint.get("/<thread_id:int>", strict_slashes=True)
@doc.summary("Fetches user information.")
def user_get(request, thread_id):
    db = request.ctx.db
    user = thread_id # For readability 

    pass # TODO: get user data

@blueprint.post("/<thread_id:int>/create", strict_slashes=True)
@doc.summary("Create a user.")
def user_create(request, thread_id):
    db = request.ctx.db
    user = thread_id # For readability 

    pass # TODO: make user


@blueprint.delete("/<thread_id:int>/delete", strict_slashes=True)
@doc.summary("Deletes a user.")
def user_delete(request, thread_id):
    db = request.ctx.db
    user = thread_id # For readability 

    pass # TODO: delete user

@blueprint.get("/<thread_id:int>/get", strict_slashes=True)
@doc.summary("Fetches all users (and info) from a channel or Guild.")
def user_mass_get(request, thread_id):
    db = request.ctx.db
    channel_or_guild = thread_id # For readability 

    pass # TODO: get every user that can see a channel or guild