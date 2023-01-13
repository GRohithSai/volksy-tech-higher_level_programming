#!/usr/bin/python3
"""It creates an empty class rectangle"""


class Rectangle:
    """It is an empty class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initailizes height and width"""
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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """set width with new value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """returns the area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)
