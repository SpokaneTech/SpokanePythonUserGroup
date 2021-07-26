from pydantic import BaseModel


class User(BaseModel):
    username: str
    token: str
    password: str
