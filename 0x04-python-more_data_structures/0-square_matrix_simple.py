#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        square = [element ** 2 for element in row]
        result.append(square)
    return result
