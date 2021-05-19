from typing import Optional
from datetime import datetime

from pydantic import BaseModel, validator


class Vehicle(BaseModel):
    vehicle_id: int
    year: int
    make: str
    model: str

    @validator('year')
    def validate_year(cls, value):
        if value < 1886:
            # See: https://www.loc.gov/everyday-mysteries/item/who-invented-the-automobile/
            raise ValueError('Vehicles didn\'t exist before 1886.')
        elif value > datetime.now().year:
            # Most current vehicle model years are at least one year in the future...
            # We'll let this one slide for now.
            return value
        else:
            return value
    

class CreateVehicle(BaseModel):
    year: int
    make: str
    model: str
