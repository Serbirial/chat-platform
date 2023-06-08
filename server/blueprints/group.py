from sanic import Blueprint

# Bits of the API
from blueprints import message, user
from server.blueprints import sse




# All of the API
api = Blueprint.group(message.blueprint,
                      user.blueprint,
                      #sse.blueprint,
                      url_prefix="/api")