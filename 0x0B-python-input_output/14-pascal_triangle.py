#!/usr/bin/python3
def pascal_triangle(n):
    """Returns a pascal triangle of n size
    Args:
        n [int]: Size of the triangle
    """
    if n <= 0:
        return [[]]

    matrix = []
    for row in range(1, n + 1):
        new = []
        for i in range(row):
            if i == 0 or i == row - 1:
                new.append(1)
            else:
                new.append(matrix[row - 2][i] + matrix[row - 2][i - 1])
        matrix.append(new)

    return matrix
