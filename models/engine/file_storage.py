#!/usr/bin/python3
"""
class storage
"""

import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():

    __file_path = "holberton.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        data = {}
        for key, value in FileStorage.__objects.items():
            if value:
                data[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile)

    def reload(self):
       """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""
       if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                data = file.read()
                for key, value in json.loads(data).items():
                    FileStorage.__objects[key] = BaseModel(**value)
