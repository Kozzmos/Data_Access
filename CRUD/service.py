from abc import ABC, abstractmethod

import pymongo

from setting import collection
from pymongo.errors import ProtocolError
from bson.objectid import ObjectId
from pprint import pprint


class BaseService(ABC):
    @abstractmethod
    def create(self, item: dict): pass

    @abstractmethod
    def get_all(self): pass


class CategoryService(BaseService):
    def create(self, item: dict):
        result = collection.insert_one(item)
        print(result)

    def get_all(self):
        # Statusu active yada modified olan kayıtları listele
        query = {
            '_BaseEntity__stats': {
                '$in': ["Active", "Modified"]
            }
        }

        projection = {
            '_id': 0,
            'name': 1,
            'description': 1
        }

        for item in collection.find(query, projection).sort(key_or_list='name'):
            pprint(item)
    # primary key
    def get_by_id(self, pk):
        query = {
            "_id": ObjectId(pk),
            '_BaseEntity__stats': {
                '$in': ['Active', 'Modified']
            }
        }
        # Sadece name ve description yazdır onu filtrele
        projection = {
            '_id': 0,
            'name': 1,
            'description': 1
        }
        # sort() fonksiyonunda sıralama yaparken default Ascendingtir
        for item in collection.find(query, projection).sort('name'):
            pprint(item)


