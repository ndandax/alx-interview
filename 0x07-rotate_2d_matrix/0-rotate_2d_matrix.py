#!/usr/bin/python3
"""
module to Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    turning a 2D matrixs
    columns into rows hence rotating
    the matrix
    """
    matrix_len = len(matrix)

    for r in range(matrix_len):
        for c in range(r, matrix_len):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    for r in range(matrix_len):
        matrix[r] = matrix[r][::-1]
        # ','.join(map(str, r))
