#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = [list(map(lambda x : x * x, obj)) for obj in matrix]
    return new_mat
