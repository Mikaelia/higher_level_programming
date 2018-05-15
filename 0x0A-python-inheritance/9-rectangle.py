#!/usr/bin/python3
class BaseGeometry():
    """base class"""

    def area(self):
        """area function"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates value"""
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """class that inherits from basegeometry"""

    def __init__(self, width, height):
        """ Initializes rectangle instance"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """returns string representation of Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """area function"""
        return self.__width * self.__height
