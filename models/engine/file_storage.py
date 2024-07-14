#!/usr/bin/python3
"""
Module for FileStorage class
"""
import json 
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Class to manage storage of hbnb models in JSON format"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as f:
            json_objects = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = value["__class__"]
                    if cls_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
                    elif cls_name == "User":
                        self.__objects[key] = User(**value)
                    # Add other classes as needed...
        except FileNotFoundError:
            pass

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, "w") as f:
            json_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(json_objects,
