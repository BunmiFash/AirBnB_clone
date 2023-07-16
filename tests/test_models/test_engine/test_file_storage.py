#!/usr/bin/python3
"""
Test Cases for FileStorage
"""
import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the file storage
    of objects.
    """
    def setUp(self):
        """
        Set Up
        """
        self.user = User()
        self.user.first_name = "Bunmi"

    def tearDown(self):
        """
        Tear Down
        """
        pass

    def test_all(self):
        """
        Tests the all method.
        """
        allObj = storage.all()
        self.assertTrue(isinstance(allObj, dict))

    def test_save(self):
        """
        Checks that an object is saved in a file
        """
        self.user.save()
        self.assertTrue(os.path.exists("file.json"))
