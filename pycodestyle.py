#!/usr/bin/python3
"""
Module to represent a simple AirBnB clone
"""
import os


class BaseModel:
    """
    Base class for all AirBnB clone objects
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize BaseModel instance
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def save(self):
        """
        Update updated_at attribute with current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return dictionary representation of BaseModel instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy

    def __str__(self):
        """
        Return string representation of BaseModel instance
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )


class User(BaseModel):
    """
    Class representing a user in the AirBnB clone
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize User instance
        """
        super().__init__(*args, **kwargs)
        

if __name__ == "__main__":
    pass
