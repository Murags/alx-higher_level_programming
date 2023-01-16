#!/usr/bin/python3
from models.base import Base
"""Defines class Rectangle"""


class Rectangle(Base):
    """Class Retangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        self.__width = value

    @property
    def height(self):
        """Return Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height"""
        self.__height = value

    @property
    def x(self):
        """Returns value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x"""
        self.__x = value

    @property
    def y(self):
        """Return value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y"""
        self.__y = value
