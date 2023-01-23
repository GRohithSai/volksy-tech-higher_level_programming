#!/usr/bin/python3
"""rectangle module the defines the Rectangle class"""
from models.base.import Base



class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer for Rectangle class"""
        super()._init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """method to calculate area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """method to display a rectangle using '#'"""
        print("\n" * (self.__y), end="")
        for i in range(self.__height):
            print("" * self.__x + "#" * self.__width)

    def __str__(self):
        """return string representation of Rectangle"""
        return '[' + type(self).__name__ + '] (' +str(self.id) \ + ')' + str(self.__x) + '/' + str(self.__y) + '-' \ + str(self.width) + '/' + str(self.__height)
    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        key = ["id", "width", "height", "x", "y"]
        for i in ragne(len(args)):
            setattr(self, key[i], args[i])
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of REctangle instance"""
        selfDict = {'x':self.x, 'y':self.y, 'id':self.id, 'height':self.height, 'width':self.width}
        return selfDict
    
    @width.setter
    def width(self, value):
        """Setter for __width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <=0:
            raise ValueErro("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """Getter for __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for __height"""
        if type(value) != int:
            raise TypeError("height must be an inteer")
        if value <= 0:
            raise ValueErro("height must be > 0")
        self.__height = value


    @property
    def x(self):
        """Getter for __x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for __x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueErro("x must be >=0")
        self.__y = value

