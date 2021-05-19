from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .users import User


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


users = [
    User(
        username = 'General Kenobi',
        token = 'Hello there',
        password = 'DEMOCRACY!'
    )
]


def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        user = [
            user
            for user
            in users
            if user.username == form_data.username \
                and user.password == form_data.password # We're truly going all-out on security here... the epitome of security. 🔒
        ][0]
    except IndexError:
        raise HTTPException(401, f'Invalid credentials.')
    else:
        return user.token


def get_user(token = Depends(oauth2_scheme)) -> User:
    try:
        user = [
            user
            for user
            in users
            if user.token == token
        ][0]
    except IndexError:
        raise HTTPException(401, f'Invalid token: {token}')
    else:
        return user
