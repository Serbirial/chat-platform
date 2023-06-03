
from sanic.blueprints import Blueprint
from sanic.response import json

from models.message import Message 
from utils import id_generator

from sanic_openapi import doc

# Create the main blueprint to work with
blueprint = Blueprint('Message_API', url_prefix="/message")


@blueprint.get("/<thread_id:int>/get/<message_id:int>", strict_slashes=True)
@doc.summary("Fetches a message from a channel or DM.")
def message_get(request, thread_id, message_id):
    db = request.ctx.db
    channel_or_user = thread_id # For readability 

    # This is a temporary implementation for the inmemory database
    data = db.get[channel_or_user]
    try:
        for msg in data:
            if msg["id"] == message_id:
                return json(msg)
        return json({"op": "void"}, status=404)

    except KeyError:
        return json({"op": "void"}, status=404)

@blueprint.delete("/<thread_id:int>/delete/<message_id:int>", strict_slashes=True)
@doc.summary("Deletes a message from a channel or DM.")
def message_delete(request, thread_id, message_id):
    pass



@blueprint.post("/<thread_id:int>/create", strict_slashes=True)
@doc.summary("Send a message to a channel or DM.")
def message_send(request, thread_id):
    db = request.ctx.db
    channel_or_user = thread_id # For readability 

    data = request.json
    _id = id_generator.generate_basic_id([x['id'] for x in db.get[channel_or_user]]) # TODO: change according to mariadb 
    # This is a temporary implementation for the inmemory database
    db.insert[channel_or_user].append({
        "content": data['content'],
        "timestamp": None,
        "parent_id": channel_or_user,
        "id": _id
    })
    return json(
        {"op": "sent"},
        status=200
    )


@blueprint.get("/<thread_id:int>/messages", strict_slashes=True)
@doc.summary("Fetches messages from a channel or DM.")
def message_mass_get(request, thread_id):
    db = request.ctx.db
    channel_or_user = thread_id # For readability 

    # This is a temporary implementation for the inmemory database
    data = db.get[channel_or_user]

    return json(data)