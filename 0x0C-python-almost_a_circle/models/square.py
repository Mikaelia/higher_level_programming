#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle

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

    @property
    def size(self):
        """size getter"""
        return self.ssizeize

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """overloads str for square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """updates instance attributes"""
        l = len(args)
        if l > 0:
            self.id = args[0]
        if l > 1:
            self.size = args[1]
        if l > 2:
            self.x = args[2]
        if l > 3:
            self.y = args[3]
        else:
            for item, value in kwargs.items():
                setattr(self, item, value)

    def to_dictionary(self):

