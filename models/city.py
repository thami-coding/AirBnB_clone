#!/usr/bin/python
"""
module for all the cities
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    class that creates cities
    """
    name = ''
    state_id = ''
