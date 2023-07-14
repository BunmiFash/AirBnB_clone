#!/usr/bin/python3
"""
Test cases for State class
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    test cases
    """
    def setUp(self):
        """
        set up class instance
        """
        self.state = State()

    def test_attr_type(self):
        """
        Checks for the type of each attribute
        """
        self.assertTrue(isinstance(self.state.name, str))
