#!/usr/bin/env python3
import os, json, sys, pickle
"""serializes instances to a JSON file\
        and deserializes JSON file to instances"""
class FileStorage:
    """Implementation"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in the __objects the obj with key <obj classname>.id"""
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as output:
            json.dump(self.__objects, output)

    def reload(self):
        """deserializes the JSON file to __objects only if JSON file\
                exists; otherwise do nothing. If the file doesn't exist\
                no exception should be raised"""
        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r') as output:
                self.__objects = json.load(output)
