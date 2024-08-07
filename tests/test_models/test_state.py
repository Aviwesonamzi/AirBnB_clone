#!/usr/bin/python3
"""Defines unittests for models/state.py."""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Unittests for testing the State class."""

    def test_attributes(self):
        state = State()
        self.assertEqual(state.name, "")

if __name__ == '__main__':
    unittest.main()
