#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel


class FileStorage():

    def __init__(self):
       self.__file_path = "holberton.json"
       self.__objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        className = obj.__class__.__name__
        key = "{className}.{id}".format(className = className, id = obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        # if self.__objects:
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, 'w') as outfile:
            json.dump(data, outfile)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = file.read()
                for key, value in json.loads(data).items():
                    self.__objects[key] = BaseModel(**value)
