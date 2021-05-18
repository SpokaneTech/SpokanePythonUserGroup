from pydantic import BaseModel


class Vehicle(BaseModel):
    vehicle_id: int
    year: int
    make: str
    model: str
