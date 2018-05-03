#!/usr/bin/python3
def print_square(size):
    """
        A function that prints out a square

        Args:
            size (int): size of the square

        Raises:
            TypeError: if size is not an integer, or if size is a float and is less than 0
            ValueError: if size is less than 0
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size == 0:
        print()
        return
    for x in range(size):
        print('#' * size)
