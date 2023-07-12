#!/usr/bin/python3
"""
Base Model module
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
    Defines all common attributes/methods
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the attributes of this instance
        and saves it to storage(a json file)
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at":
                    """
                    convert date in string into datetime object
                    """
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Prints string representation of an object.
        """
        return ("[{}] [{}] {}".format(
            type(self).__name__, self.id, self.__dict__
            ))

    def save(self):
        """
        Saves this instance to storage(a json file) and
        updates the updated_at attribute
        """
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dicctionary containing all the keys/values of
        an instance.
        """
        dictObj = self.__dict__.copy()
        dictObj["__class__"] = type(self).__name__
        dictObj["created_at"] = dictObj["created_at"].isoformat()
        dictObj["updated_at"] = dictObj["updated_at"].isoformat()
        return dictObj
