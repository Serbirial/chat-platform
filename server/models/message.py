from models.user import User

class Message(object):
    def __init__(self, id: int, parent_id: int, content: str, author_id: int, timestamp: float):
        self.id = id
        self.parent_id = parent_id
        self.content = content
        self.author = author_id
        self.timestamp = timestamp