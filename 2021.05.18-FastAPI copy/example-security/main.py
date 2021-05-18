from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

from .vehicles import Vehicle


app = FastAPI()


vehicles: list[Vehicle] = [
    Vehicle(
        vehicle_id = 1,
        year = 2003,
        make = 'Mitsubishi',
        model = 'Montero Sport'
    )
]


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@app.get('/vehicles/', response_model=list[Vehicle])
def get(token: str = Depends(oauth2_scheme)):
    return vehicles
