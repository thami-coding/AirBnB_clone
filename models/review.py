#!/usr/bin/python
"""
module for all the reviews
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    class that creates reviews instances
    """
    place_id = ''
    user_id = ''
    text = ''
