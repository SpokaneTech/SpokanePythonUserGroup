from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .users import User


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


users = [
    User(
        username = 'General Kenobi',
        token = 'Hello there',
    )
]


def get_user(token = Depends(oauth2_scheme)) -> User:
    try:
        user = [
            user
            for user
            in users
            if user.token == token # Wow, such security. Very impressive.
        ][0]
    except IndexError:
        raise HTTPException(401, f'Invalid token: {token}')
    else:
        return user
