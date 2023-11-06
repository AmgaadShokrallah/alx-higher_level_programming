#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for d in range(len(matrix)):
        for j in range(len(matrix[d])):
                print("{:d}".format(matrix[d][j]), end="")
                if j != (len(matrix[d]) - 1):
                    print(" ", end="")


        print("")
