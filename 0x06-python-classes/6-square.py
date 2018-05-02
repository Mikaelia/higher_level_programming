#!/usr/bin/python3
class Square:
    """A square class"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
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
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple:
            for x in value:
                if type(x) is not int or x < 0 or len(value) is not 2:
                    raise TypeError(
                        "position must be a tuple of 2 positive integers")
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        if self.__position[1]:
            print(' ' * self.__position[1])
        for x in range(self.__size):
            if self.__postion[0]:
                print(' ' * self.__position[0], end='')
            for y in range(self.__size):
                if y == (self.__size - 1):
                    print('#')
                else:
                    print('#', end='')
