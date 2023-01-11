#!/usr/bin/python3
def square_matrix_sample(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        row = list(map(lambda x: x * x, matrix[i]))
        new_matrix.append(row)
    return new_matrix
