#!/usr/bin/python3
"""Defines class BaseGeometry"""


class BaseGeometry:
    """Representing BaseGeometry"""
    def area(self):
        """Raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks value"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
