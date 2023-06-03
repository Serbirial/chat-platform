from sanic import Blueprint

# Bits of the API
from blueprints import message




# All of the API
api = Blueprint.group(message.blueprint,
                            
                            url_prefix="/api")