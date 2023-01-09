#!/usr/bin/python3:
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        row = matrix[i]]
        for j in range(len(row)):
            print("{:d}".format(row[j]), end='')
            if (j != len(row) - 1)
            print(" ", end='')
        print()
