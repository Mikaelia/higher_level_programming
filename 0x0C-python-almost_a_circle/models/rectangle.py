#!/usr/bin/python3
"""The rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation of Rectangle class
            Args:
                width(int): width of the rectangle
                height(int): height of the rectangle
                x(int)
                y(int)
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """finds area"""
        return self.__height * self.__width
        if value < 0:
            ValueError('x must be >= 0')

    def display(self):
        """prints rectangle"""
        print("\n" * self.__y, end='')
        for x in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """overloads str method"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.__x,
                                                        self.__y,
                                                        self.__width,
                                                        self.__height))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        l = len(args)
        if l > 0:
            self.id = args[0]
        if l > 1:
            self.__width = args[1]
        if l > 2:
            self.__height = args[2]
        if l > 3:
            self.__x = args[3]
        if l > 4:
            self.__y = args[4]
        else:
            for name, value in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self):
        """returns a dictionary"""
        d = dict(vars(self))
        s = len(type(self).__name__) + 3
        for key in vars(self):
            if key is not 'id':
                d[key[s:]] = d.pop(key)
        return d
