from fastapi import Depends, FastAPI

from .auth import get_token, get_user
from .users import User


app = FastAPI()


@app.get('/token/')
def login(token = Depends(get_token)):
    return {
        'access_token': token,
        'token_type': 'bearer',
    }


@app.get('/me/')
def get(user: User = Depends(get_user)):
    return user.username
