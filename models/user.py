#!/usr/bin/python3
"""
this module contains one
class user that creates a new user
"""

import datetime
from models.base_model import BaseModel


class User(BaseModel):
    """
    creates a new user and stores
    their information in a json file
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):

        if kwargs:
            dct = {}
            parent_attrs = ['id', 'created_at', 'updated_at']
            for key, value in kwargs.items():
                if key in parent_attrs:
                    dct[key] = value
                elif key != "__class__":
                    setattr(User, key, value)
            super().__init__(**dct)
        else:
            super().__init__()

    def __str__(self):
        return BaseModel.__str__(self)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        BaseModel.save(self)

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        cls_dict = User.__dict__
        cls_attr = ['email', 'password', 'first_name', 'last_name']
        user_dict = BaseModel.to_dict(self)
        for key, value in cls_dict.items():
            if key in cls_attr:
                user_dict[key] = value
        return user_dict
