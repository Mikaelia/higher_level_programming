#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix

    Args:
        matrix (matrix): Matrix to divide
        div (int or float): Value to divide elements by

    Returns:
        New matrix with divided values, rounded to 2 decimal places

    Raises:
        TypeError: If div not a number, or each row of matrix not same size,
            or not matrix of integers/floats
        ZeroDivisionError: If div is equal to 0
    """

    new_matrix = []

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = list(map(list, matrix))

    for i, row in enumerate(new_matrix):
        if len(new_matrix[0]) != len(new_matrix[i]):
            raise TypeError('Each row of the matrix must have the same size')
        for i, val in enumerate(row):
            if type(val) is not int and type(val) is not float:
                  raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            row[i] = round(val / div, 2)
    return(new_matrix)
