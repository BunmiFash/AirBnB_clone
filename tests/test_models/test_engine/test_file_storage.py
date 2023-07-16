#!/usr/bin/python3
"""
Test Cases for FileStorage
"""
import unittest
import os
import pep8
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

    def test_pep8_file_storage(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
