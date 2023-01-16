#!/usr/bin/python3
"""Defines class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns width/ height"""
        return self.width

    @size.setter
    def size(self, value):
        """sets width and height"""
        self.width = value
        self.height = value

    def __str__(self):
        """representation of Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
