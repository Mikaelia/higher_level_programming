#!/usr/bin/python3
def pascal_triangle(n):
    """Returns a pascal triangle of n size
    Args:
        n [int]: Size of the triangle
    """
    if n <= 0:
        return []

    arrays = []
    for row in range(1, n + 1):
        new = []
        for i in range(row):
            if i == 0 or i == row - 1:
                new.append(1)
            else:
                new.append(arrays[row - 2][i] + arrays[row - 2][i - 1])
        arrays.append(new)

    return arrays
