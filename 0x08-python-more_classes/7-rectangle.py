#!/usr/bin/python3
class Rectangle:
    """
    A rectangle class

    Raises:
        TypeError if width or height is not an integer
        ValueError if width or height is less than zero
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        gets width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """
        gets height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets height
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.height == 0:
            return (0)
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        returns string representation of rectangle
        """
        new_str = ''
        if self.__width == 0 or self.__height == 0:
            return(new_str)
        new_str += (str(self.print_symbol) * self.__width +
                    '\n') * (self.__height - 1)
        new_str += str(self.print_symbol) * self.__width
        return new_str

    def __repr__(self):
        """
        returns string representation of rectangle
        """
        return "Rectangle({},{})".format(self.__width, self.__height)

    def __del__(self):
        """
        prints message upon deletion of rectange
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
