#!/usr/bin/python3

def matrix_divided(matrix, div):

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    size = []

    for lst in matrix:
        if not isinstance(lst, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        size.append(len(lst))
    size = set(size)
    if not (len(size) == 1):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    error = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        templist = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error)
            templist.append(round(element / div, 2))
        new_matrix.append(templist)

    return new_matrix
