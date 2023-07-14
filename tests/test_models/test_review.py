#!/usr/bin/python3
"""
Test cases for Review class
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    test cases
    """
    def setUp(self):
        """
        set up class instance
        """
        self.review = Review()

    def test_attr_type(self):
        """
        Checks for the type of each attribute
        """
        self.assertTrue(isinstance(self.review.place_id, str))
        self.assertTrue(isinstance(self.review.user_id, str))
        self.assertTrue(isinstance(self.review.text, str))
