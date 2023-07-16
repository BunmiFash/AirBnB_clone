#!/usr/bin/python3
"""
Test Cases for Base Model
"""
import unittest
from io import StringIO
from models.base_model import BaseModel
from datetime import datetime


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
        self.base.save()
        self.assertGreater(self.base.updated_at, self.base.created_at)

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
