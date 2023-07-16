#!/usr/bin/python3
"""
Test cases for User class
"""
import unittest
from models.user import User


class TestCity(unittest.TestCase):
    """
    test cases
    """
    def setUp(self):
        """
        set up class instance
        """
        self.user = User()

    def test_attr_type(self):
        """
        Checks for the type of each attribute
        """
        self.assertTrue(isinstance(self.user.email, str))
        self.assertTrue(isinstance(self.user.password, str))
        self.assertTrue(isinstance(self.user.first_name, str))
        self.assertTrue(isinstance(self.user.last_name, str))
