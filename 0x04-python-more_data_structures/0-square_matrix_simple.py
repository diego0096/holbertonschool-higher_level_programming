#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new = []
        for r in matrix:
            new.append([a ** 2 for n in r])
    return new
