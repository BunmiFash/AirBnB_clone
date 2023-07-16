#!/usr/bin/python3
"""
Test cases for Amenity class
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    test cases
    """
    def setUp(self):
        """
        set up class instance
        """
        self.amenity = Amenity()

    def test_attr_type(self):
        """
        Checks for the type of each attribute
        """
        self.assertTrue(isinstance(self.amenity.name, str))
