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

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

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
        """
        method reload
        """

        my_dict = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'State': State, 'City': City, 'Amenity': Amenity,
                   'Review': Review}
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as q:
                other_dict = json.loads(q.read())
                for key, val in other_dict.items():
                    self.new(my_dict[val['__class__']](**val))
