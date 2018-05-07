#!/usr/bin/python3
class Rectangle:
    """
    A rectangle class

    Raises:
        TypeError if width or height is not an integer
        ValueError if width or height is less than zero
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """
        returns the area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.height == 0:
            return (0)
        return (self.__width * 2 + self.__height * 2)
