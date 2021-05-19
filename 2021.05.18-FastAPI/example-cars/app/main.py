from fastapi import FastAPI, HTTPException
from fastapi.params import Depends

from .auth import get_token, get_user
from .db_context import DbContext
from .vehicles import CreateVehicle, Vehicle


app = FastAPI()


@app.get('/token/')
def login(token = Depends(get_token)):
    return {
        'access_token': token,
        'token_type': 'bearer',
    }


@app.get('/me/')
def get(user = Depends(get_user)):
    return user.username


@app.get('/vehicles/', dependencies=[Depends(get_user)], response_model=list[Vehicle])
def list_vehicles(db_context = Depends(DbContext)):
    vehicles = db_context.list_vehicles()
    return vehicles


@app.get('/vehicles/{vehicle_id}/', dependencies=[Depends(get_user)], response_model=Vehicle)
def get_vehicle(vehicle_id: int, db_context = Depends(DbContext)):
    vehicle = db_context.get_vehicle(vehicle_id)
    if vehicle is None:
        return HTTPException(404, f'No vehicle with ID {vehicle_id} found.')
    return vehicle


@app.post('/vehicles/', dependencies=[Depends(get_user)], response_model=str)
def create_vehicle(data: CreateVehicle, db_context = Depends(DbContext)):
    try:
        vehicle_id = db_context.add_vehicle(data)
    except Exception:
        return HTTPException(400, data)
    return f'/vehicles/{vehicle_id}/'
