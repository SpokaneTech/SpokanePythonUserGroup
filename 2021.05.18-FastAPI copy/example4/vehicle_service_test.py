from .vehicle_service import VehicleService
from .vehicles import Vehicle


def test__vehicle_service__init__doesnt_throw_error():
    _ = VehicleService()


def test__vehicle_service__vehicles__returns_vehicles_from_csv_file():
    vehicle_service = VehicleService()

    expected = [
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
    assert vehicle_service.vehicles == expected
