#!/usr/bin/python3
"""
Test cases for Place class
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    test cases
    """
    def setUp(self):
        """
        set up class instance
        """
        self.place = Place()

    def test_attr_type(self):
        """
        Checks for the type of each attribute
        """
        self.assertTrue(isinstance(self.place.city_id, str))
        self.assertTrue(isinstance(self.place.city_id, str))
        self.assertTrue(isinstance(self.place.user_id, str))
        self.assertTrue(isinstance(self.place.name, str))
        self.assertTrue(isinstance(self.place.description, str))
        self.assertTrue(isinstance(self.place.number_rooms, int))
        self.assertTrue(isinstance(self.place.number_bathrooms, int))
        self.assertTrue(isinstance(self.place.max_guest, int))
        self.assertTrue(isinstance(self.place.price_by_night, int))
        self.assertTrue(isinstance(self.place.latitude, float))
        self.assertTrue(isinstance(self.place.longitude, float))
        self.assertTrue(isinstance(self.place.amenity_ids, list))
