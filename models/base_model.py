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
        cls_name = type(self).__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        dictionary = {}
        for k, v in self.__dict__.items():
            if type(v) == datetime:
                dt = [v.year, v.month, v.day, v.hour, v.minute, v.second]
                dictionary[k] = datetime(*dt).isoformat()
                continue
            dictionary[k] = v
        dictionary["__class__"] = type(self).__name__
        return dictionary
