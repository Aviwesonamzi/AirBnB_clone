#!/usr/bin/python3
"""Defines unittests for models/city.py."""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Unittests for testing the City class."""

    def test_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

if __name__ == '__main__':
    unittest.main()
