#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared = []
    for row in matrix:
        squared.append([i**2 for i in row])
    return squared
