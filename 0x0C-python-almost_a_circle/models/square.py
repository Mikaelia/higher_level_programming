#!/usr/bin/python3
"""square module"""
from rectangle import Rectangle

class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Square constructor
            Args:
                size(int): size of the square
                x(int): positional offset
                y(int): positional offset
                id(int): instance id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        "to string for square"
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        'size getter'
        return self.height

    @size.setter
    def size(self, value):
        "size setter"
        self.width = value
        self.height = value

