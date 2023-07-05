#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda x: x**2, row)), matrix))

#explanation 
''' The square_matrix_map function takes a matrix (a 2-dimensional array) as a parameter.

The function uses map to apply a lambda function to each row of the matrix. The lambda function takes each element x in the row and computes its square x**2.

The result of the inner map operation is converted back to a list using list.

The outer map operation applies the lambda function to each row of the matrix, resulting in a new matrix where each value is the square of the corresponding value in the input matrix.

Finally, the new matrix is returned.

This implementation follows the specified requirements, using map and lambda functions to calculate the square values of the integers in the matrix. The initial matrix is not modified, and no external modules are imported. The code is kept within three lines as specified. '''
