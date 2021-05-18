from fastapi import Depends, FastAPI

from .auth import get_user
from .users import User


app = FastAPI()


@app.get('/me/')
def get(user: User = Depends(get_user)):
    return user.username
