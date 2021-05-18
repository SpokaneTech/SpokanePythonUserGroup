from fastapi import FastAPI, HTTPException

from .vehicles import CreateVehicle, Vehicle


app = FastAPI()


vehicles: list[Vehicle] = []


montero_sport = Vehicle(
    vehicle_id = 1,
    year = 2003,
    make = 'Mitsubishi',
    model = 'Montero Sport'
)
vehicles.append(montero_sport)


@app.get('/vehicles/', response_model=list[Vehicle])
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
def create_vehicle(data: CreateVehicle):
    vehicle_id = len(vehicles) + 1
    vehicle = Vehicle(
        vehicle_id = vehicle_id,
        **data.dict(),
    )
    vehicles.append(vehicle)
