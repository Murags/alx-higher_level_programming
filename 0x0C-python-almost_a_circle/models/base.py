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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return string representation"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the string representation to a file"""
        filename = cls.__name__ + ".json"
        result = []
        if list_objs:
            for i in list_objs:
                result.append(cls.to_dictionary(i))

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(result))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string."""
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        try:
            filename = str(cls.__name__) + ".json"
            result = []
            if not filename:
                return result
            else:
                with open(filename, "r", encoding="utf-8") as f:
                    data = cls.from_json_string(f.read())

                for i in data:
                    result.append(cls.create(**i))
                return result
        except Exception:
            return []
