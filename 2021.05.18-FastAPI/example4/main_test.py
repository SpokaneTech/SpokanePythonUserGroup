from fastapi.testclient import TestClient

from .main import app
from .vehicles import Vehicle


client = TestClient(app)


def test__app__list_vehicles():
    response = client.get('/vehicles/')

    vehicles = [
        Vehicle(
            vehicle_id = 1,
            year = 2003,
            make = 'Mitsubishi',
            model = 'Montero',
        ),
        Vehicle(
            vehicle_id = 2,
            year = 2007,
            make = 'Toyota',
            model = '4Runner',
        ),
    ]
    expected = [
        vehicle.dict()
        for vehicle
        in vehicles
    ]

    assert response.status_code == 200
    assert response.json() == expected
