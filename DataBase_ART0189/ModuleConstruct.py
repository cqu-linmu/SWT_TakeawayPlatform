from pydantic import BaseModel

class User(BaseModel):
    account: str
    screen_name: str
    hash_pwd: str