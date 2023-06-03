import json

from sanic import Sanic, Blueprint
from sanic_openapi import swagger_blueprint
# MODELS #
from models import message

# BLUEPRINTS #
from blueprints.group import api

# UTILS #
from utils import db
from utils import inmemory

# Webserver
app = Sanic(__name__)

# Add DB
_db = inmemory.InMemoryDatabase()

# Add all the blueprints

# Api (V1)
app.blueprint(api)


# Inject the DB
@app.on_request
async def setup_db_connection(request):
    request.ctx.db = _db

#@app.main_process_start
#async def main_process_start(app):
#    _db = db.DB(db.mariadb_pool(0)) # Create the connection to the DB
#    _db = inmemory.InMemoryDatabase()
#    app.ctx.db = _db


# Close the DB on exit
#@app.main_process_stop
#async def close_db(app, loop):
#    _db.pool.close()


# API V1 #

if __name__ == '__main__':

    app.run(host='localhost', port=42042, debug=True)