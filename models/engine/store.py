#!/usr/bin/python3
"""
File Storage for all data
"""
import json
import os
from models.base_model import BaseModel


class FileStorage():
    """
    Serializes instances to a JSON file
    and desrializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        set attribute of of __object dict
        """
        cls = type(obj).__name__
        key = "{}.{}".format(cls, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        ie save objects to the json file
        """
        objDict = {}
        for key, value in self.__objects.items():
            objDict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(objDict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as fi:
                obj = json.load(fi)
            for key, val in obj.items():
                self.__objects[key] = eval(val["__class__"])(**val)
