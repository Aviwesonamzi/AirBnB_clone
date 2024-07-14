#!/usr/bin/python3
"""Defines unittests for models/review.py."""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Unittests for testing the Review class."""

    def test_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

if __name__ == '__main__':
    unittest.main()
