import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def test_instance_creation(self):
        """
        Test that an instance of User is created correctly.
        """
        user = User()
        self.assertIsInstance(user, User)

    def test_initial_attributes(self):
        """
        Test that the initial attributes of User are set correctly.
        """
        user = User()
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)

    # Add more test cases to cover all functionalities of User

if __name__ == '__main__':
    unittest.main()
