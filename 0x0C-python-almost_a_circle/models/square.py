#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """A Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Square class constructor
            Args:
                size(int): size of square
                x(int): position offset
                y(int): position offset
                id(int): instance id
        """
        super().__init__(size, size, x, y, id)
    def __str__(self):
        """overloads str method"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.height))
