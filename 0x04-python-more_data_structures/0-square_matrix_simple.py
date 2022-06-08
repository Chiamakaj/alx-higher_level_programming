#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        print ()
    return [list(map(lambda x : x * x, obj)) for obj in matrix]
