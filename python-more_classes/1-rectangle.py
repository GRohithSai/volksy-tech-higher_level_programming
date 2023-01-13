#!/usr/bin/python3
"""It is a class that defines a rectangle"""


class Rectangle:
    """Defines an empty class Rectangle"""

    def __init__(self, width=0, height=0):
        """Iniatilizes height and width"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @height.setter
    def height(self, value):
        """set height with new value"""
        if type(value) is not int:
            raise TypeError("height must be an inteer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__value = value

    @width.setter
    def width(self, value):
        """set width with new value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
