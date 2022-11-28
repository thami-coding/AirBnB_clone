#!/usr/bin/python3
"""
The file_storage module has one class FileStorage
that serializes instances to a JSON file and
deserializes JSON file to instances
"""


from datetime import datetime
import json
from os.path import exists


class FileStorage:
    """
    FileStorage class serializes instances to a
    JSON file and deserializes JSON file to instances
    """

    def __init__(self, file_path, objects):
        self.file_path = file_path
        self.objects = objects

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, file_path):
        self.__file_path = file_path

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, objects):
        self.__objects = objects

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key
        <obj class name>.id
        """
        key = type(obj).__name__ + '.' + obj.id
        obj.created_at = datetime.isoformat(obj.created_at)
        obj.updated_at = datetime.isoformat(obj.updated_at)
        self.__objects[key] = obj.__dict__

    def save(self):
        """
        serializes __objects to the JSON
        file (path: __file_path)
        """
        objcts = self.__objects
        filename = self.__file_path
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(objcts, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        filename = self.__file_path
        if exists(filename):
            with open(filename, 'r+', encoding="utf-8") as f:
                self.__objects = json.load(f)
