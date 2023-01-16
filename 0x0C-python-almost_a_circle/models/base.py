#!/usr/bin/python3
"""Defines class Base"""
import json


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Return string representation"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
