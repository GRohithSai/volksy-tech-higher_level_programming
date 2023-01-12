#!/usr/bin/python3
"""creating class"""


class Square:
    """Square with private instance attribute and instantiation"""
    def __init__(self, size=0):
        """initailize data"""
        self.__size=size

    def area(self):
        """return square area"""
        return(self.__size ** 2)
        
    @property
    def size(self):
        """retrieve size"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """handling errors"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
