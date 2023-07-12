#!/usr/bin/python3
""" FileStorage Module """
import json
import os


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
               obj.to_dict()
        )

    def save(self):
        """
        Serializes __objects dictionary to a json file
        """
        with open(self.__file_path, 'w', encoding='utf-8') as json_file:
            json.dump(self.__objects, json_file)

    def reload(self):
        """
        Deserializes object from a json file if it exists
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as json_file:
                self.__objects = json.load(json_file)
