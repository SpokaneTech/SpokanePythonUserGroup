from __future__ import annotations

from pymongo import MongoClient
import pymongo
from pymongo.database import Database
from pymongo.collection import Collection

from .vehicles import CreateVehicle


class DbContext():

    def get_vehicle(self, vehicle_id: int):
        collection = self._get_cars_collection()
        document = collection.find_one({ 'vehicle_id': vehicle_id })
        if document is not None:
            document.pop('_id', None)
        return document

    def list_vehicles(self):
        collection = self._get_cars_collection()
        documents = list(collection.find())
        for document in documents:
            document.pop('_id', None)
        return documents

    def add_vehicle(self, vehicle: CreateVehicle):
        collection = self._get_cars_collection()
        try:
            document = next(collection.find({ 'vehicle_id': 1 }) \
                .sort('vehicle_id', direction=pymongo.DESCENDING))
            vehicle_id = int(document['vehicle_id']) + 1
        except Exception:
            vehicle_id = 1

        document = vehicle.dict()
        document['vehicle_id'] = vehicle_id
        collection.insert_one(document)
        return vehicle_id

    def _get_cars_collection(self) -> Collection:
        mongo_client = MongoClient('mongodb://root:example@mongo:27017/?authSource=admin')
        db: Database = mongo_client.test_database
        collection: Collection = db.cars
        return collection
