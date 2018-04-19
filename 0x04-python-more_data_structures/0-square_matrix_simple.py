#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    smatrix = []
    for row in matrix:
        smatrix.append(list(map(lambda x: x**2, row)))
    return smatrix
