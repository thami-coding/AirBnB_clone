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
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return type(self).__objects

    def new(self, obj):
        """
        sets in __objects the obj with key
        <obj class name>.id
        """
        key = type(obj).__name__ + '.' + obj.id
        type(self).__objects[key] = obj.__dict__

    def save(self):
        """
        serializes __objects to the JSON
        file (path: __file_path)
        """
        objects = type(self).__objects
        for _, val in objects.items():
            for k, v in val.items():
                if type(v) == datetime:
                    val[k] = datetime.isoformat(v)

        filename = type(self).__file_path
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(objects, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        filename = type(self).__file_path
        if exists(filename):
            with open(filename, 'r+', encoding="utf-8") as f:
                type(self).__objects = json.load(f)
