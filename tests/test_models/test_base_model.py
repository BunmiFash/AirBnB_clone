#!/usr/bin/python3
"""
Test Cases for Base Model
"""
import unittest
import pep8
from io import StringIO
from models.base_model import BaseModel
from datetime import datetime
import models


class TestBaseModel(unittest.TestCase):
    """
    All test cases for base model
    """
    """
     Test to check for data types
    """
    def setUp(self):
        """
        Base Model instances
        """
        self.base = BaseModel()
        self.base.level = "300"
        self.base.dept = "MLS"

        baseKwargs = self.base.to_dict()
        self.newBase = BaseModel(**baseKwargs)

    def tearDown(self):
        """
        Tear Down
        """
        pass

    def test_id_str(self):
        """
        Checks that id is string
        """
        self.assertTrue(type(self.base.id) == str)

    def test_created_at_date(self):
        """
        Checks that created_at is a datetime attribute
        """
        self.assertTrue(type(self.base.created_at) == datetime)

    def test_updated_at_date(self):
        """
        Checks that updated_at is a datetime attribute
        """
        self.assertTrue(type(self.base.updated_at) == datetime)

    def test_save(self):
        """
        Test the time difference between created_at and
        updated_at
        """
        all_objects = models.storage.all()
        self.base.save()
        key = "BaseModel" + '.' + self.base.id
        self.assertGreater(self.base.updated_at, self.base.created_at)
        self.assertNotEqual(self.base.updated_at, self.base.created_at)
        self.assertIn(key, all_objects)

    def test_to_dict(self):
        """
        Check for the presence of keys in the dictionary
        """
        self.base.name = "Jeniffer"
        self.base.age = 29
        baseDict = self.base.to_dict()
        self.assertIn('created_at', baseDict)
        self.assertIn('id', baseDict)
        self.assertIn('updated_at', baseDict)
        self.assertIn('__class__', baseDict)
        self.assertIn('name', baseDict)
        self.assertIn('age', baseDict)

        self.assertTrue(isinstance(baseDict, dict))

    def test_kwargs_attr(self):
        """
        Checks for the presence of attributes in an object
        created from kwargs
        """
        self.assertIn('id', self.newBase.__dict__)
        self.assertIn('created_at', self.newBase.__dict__)
        self.assertIn('updated_at', self.newBase.__dict__)
        self.assertIn('level', self.newBase.__dict__)
        self.assertIn('dept', self.newBase.__dict__)
        self.assertNotIn('__class__', self.newBase.__dict__)

    def test_datetime_from_kwargs(self):
        """
        checks the data type of created_at and
        updated_at from kwargs
        """
        self.assertTrue(type(self.newBase.created_at), datetime)
        self.assertTrue(type(self.newBase.updated_at), datetime)

    def test_pep8_base_model(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
