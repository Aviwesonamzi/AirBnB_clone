#!/usr/bin/python3
"""
Module for FileStorage class
"""

import json
from models.base_model import BaseModel


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
            with open(self.__file_path, 'r') as f:
                json_objects = json.load(f)
                for k, v in json_objects.items():
                    cls_name = v['__class__']
                    self.__objects[k] = eval(cls_name)(**v)
        except FileNotFoundError:
            pass
