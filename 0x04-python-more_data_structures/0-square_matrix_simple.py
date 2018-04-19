#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[element**2 for element in matrix[i]] for i in range(len(matrix))]
