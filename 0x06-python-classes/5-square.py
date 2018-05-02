#!/usr/bin/python3
class Square:
    """A square class"""

    def __init__(self, size=0):
        """Initializes instance of Square
        Args:
            size (int): size of square
        """
        self.size = size

    @property
    def size(self):
        """gets size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """finds area"""
        return self.__size ** 2

    def my_print(self):
        """prints out square"""
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    if y == (self.__size - 1):
                        print('#')
                    else:
                        print('#', end='')
