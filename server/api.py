import json

from sanic import Sanic
from asyncio import Queue
# MODELS #
from models import message

# BLUEPRINTS #
from blueprints.group import api

# UTILS #
from utils import db
from utils import redis
from utils import hashing

# Webserver
app = Sanic(__name__)

# Add DB, Redis, Hasher
_db = db.DB(db.mariadb_pool(0)) # Create the connection to the DB
_redis = redis.RDB
_hasher = hashing.Hasher()

# Add all the blueprints

# Api (V1)
app.blueprint(api)


# Inject the DB
@app.on_request
async def setup_db_connection(request):
    request.ctx.db = _db
    request.ctx.redis = _redis
    request.ctx.hasher = _hasher

@app.main_process_start
async def main_process_start(app):
    app.ctx.sse_queue = Queue()


# Close the DB on exit
#@app.main_process_stop
#async def close_db(app, loop):
#    _db.pool.close()


# API V1 #

if __name__ == '__main__':

    app.run(host='localhost', port=42042, debug=False, access_log=False)