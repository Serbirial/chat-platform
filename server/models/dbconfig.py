from dataclasses import dataclass

@dataclass
class DBConfig:
    host = '127.0.0.1'
    port = 3306
    user: str
    password: str
    database: str
    pool_size = 20