#!/usr/bin/python3
class Square:
    """A square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes instance of Square
        Args:
            size (int): size of square
            position (tuple): position of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets size, and sets to an integer greater than zero"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """gets property and sets it as tuple with positive ints"""
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple):
            for x in value:
                if isinstance(x, int) and x >= 0 and len(value) is 2:
                    self.__position = value
                    return
        raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """finds area"""
        return self.__size ** 2

    def my_print(self):
        """prints out square"""
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for x in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
