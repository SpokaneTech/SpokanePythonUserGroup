from fastapi import FastAPI, HTTPException
from fastapi.params import Depends

from .vehicles import Vehicle
from .vehicle_service import VehicleService


app = FastAPI()



@app.get('/vehicles/', response_model=list[Vehicle])
def list_vehicles(vehicle_service = Depends(VehicleService)):
    vehicles = vehicle_service.vehicles
    return vehicles
