from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


# Let's create a Pydantic vehicle model
class Vehicle(BaseModel):
    vehicle_id: int # avoid using `id` as it is a built-in python function
    year: int
    make: str
    model: str


# All about that type hinting...
vehicles: list[Vehicle] = []


# Nit: __init__ does not have type hinting / IntelliSense with Pydantic
# see: https://github.com/microsoft/python-language-server/issues/1898
montero_sport = Vehicle(
    vehicle_id = 1,
    year = 2003,
    make = 'Mitsubishi',
    model = 'Montero Sport'
)
vehicles.append(montero_sport)


@app.get('/vehicless/', response_model=list[Vehicle])
def list_vehicles():
    return vehicles


@app.get('/vehicles/{vehicle_id}/', response_model=Vehicle)
def get_vehicle(vehicle_id: int):
    vehicle_index = vehicle_id - 1
    try:
        vehicle = vehicles[vehicle_index]
    except IndexError:
        return HTTPException(404, 'Can\'t find a vehicle with that ID!')
    else:
        return vehicle


@app.post('/vehicles/')
def create_vehicle(data: Vehicle):
    # Uh-h, somethings off...
    vehicles.append(data)
