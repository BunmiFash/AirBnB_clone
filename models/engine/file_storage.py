#!/usr/bin/python3
""" FileStorage Module """
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
        Serializes instances to a JSON file
        Deserializes a JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the __objects dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the __object dictionary
        using its class name and id as a key
        """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = (
               obj
        )

    def save(self):
        """
        Serializes __objects dictionary to a json file
        """
        """
        - created a new dictionary to store the objects
        - converted each value to dict format to enable serialization
        """
        obj = {}
        for key, value in self.__objects.items():
            obj[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as json_file:
            json.dump(obj, json_file)

    def reload(self):
        """
        Deserializes object from a json file if it exists
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as json_file:
                obj = json.load(json_file)
            for key, val in obj.items():
                self.__objects[key] = eval(val["__class__"])(**val)
