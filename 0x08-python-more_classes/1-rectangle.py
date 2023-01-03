#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """Initialize the rectangle with an optional width and height.

        Args:
          width (int, optional): The width of the rectangle. Defaults to 0.
          height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self._width
    @width.setter
    def width(self, width):
        """Set the width of the rectangle.

        Args:
          value (int): The new width of the rectangle.

        Raises:
          TypeError: If the width is not an integer.
          ValueError: If the width is less than 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self._width = width

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self._height
    @height.setter
    def height(self, height):
        """Set the height of the rectangle.

        Args:
          value (int): The new height of the rectangle.

        Raises:
          TypeError: If the height is not an integer.
          ValueError: If the height is less than 0.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self._height = height
