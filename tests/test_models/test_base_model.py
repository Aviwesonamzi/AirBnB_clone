import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_instance_creation(self):
        """
        Test that an instance of BaseModel is created correctly.
        """
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)

    def test_initial_attributes(self):
        """
        Test that the initial attributes of BaseModel are set correctly.
        """
        instance = BaseModel()
        self.assertIsNotNone(instance.id)
        self.assertIsNotNone(instance.created_at)
        self.assertIsNotNone(instance.updated_at)


if __name__ == '__main__':
    unittest.main()
