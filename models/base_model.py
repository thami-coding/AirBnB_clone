#!/usr/bin/python3
"""
This is the base model that has one class
BaseModel that defines all common attributes/methods
for other classes
"""


from datetime import datetime
import uuid


class BaseModel:
    """
    BaseModel that defines all common
    attributes/methods for other classes
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dictionary = {}
        for k, v in self.__dict__.items():
            if type(v) == datetime:
                dt = [v.year, v.month, v.day, v.hour, v.minute, v.second]
                dictionary[k] = datetime(*dt).isoformat()
                continue
            dictionary[k] = v
        dictionary["__class__"] = type(self).__name__
        return dictionary
