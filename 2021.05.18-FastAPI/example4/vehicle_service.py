

from .vehicles import Vehicle


class VehicleService():

    @property
    def vehicles(self):
        return self._vehicles

    def __init__(self) -> None:
        vehicles = []

        with open('vehicles.csv', 'r') as infile:
            lines = [
                line.strip()
                for line
                in infile.readlines()
            ]

        columns = lines[0].split(',')
        del lines[0]

        for line in lines:
            item = {}
            values = line.split(',')
            for key, value in zip(columns, values):
                item[key] = value
            vehicle = Vehicle(**item)
            vehicles.append(vehicle)
        
        self._vehicles = vehicles
