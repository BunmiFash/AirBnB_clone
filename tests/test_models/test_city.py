#!/usr/bin/python3
"""
Test cases for City class
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    test cases
    """
    def setUp(self):
        """
        set up class instance
        """
        self.city = City()

    def test_attr_type(self):
        """
        Checks for the type of each attribute
        """
        self.assertTrue(isinstance(self.city.name, str))
        self.assertTrue(isinstance(self.city.state_id, str))
