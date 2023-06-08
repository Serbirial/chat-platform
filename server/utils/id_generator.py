import secrets
import uuid

def generate_user_id(db_conn):
    while 1:
        _id = secrets.randbits(64)
        check = db_conn.query_row("SELECT id FROM users WHERE id=?", _id)
        if not check:
            return _id
            break

def generate_message_id(db_conn):
    while 1:
        _id = secrets.randbits(64)
        check = db_conn.query_row("SELECT id FROM messages WHERE id=?", _id)
        if not check:
            return _id
            break

def generate_session_token(redis_conn, author_id):
    data = redis_conn.get(author_id)
    _id = str(uuid.uuid4())
    if not data:
        redis_conn.set(author_id, _id)
    return _id

def get_session_token(redis_conn, author_id):
    data = redis_conn.get(author_id)
    if not data:
        return False
    return str(data)

