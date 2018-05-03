#!/usr/bin/python3
"""
This module divides two list
"""


def matrix_divided(matrix, div):
    """
    Divides two list inside the matrix
    if the
    Args:
        a: input variable
        b: input variable default to 98 if none
    Raises:
        TypeError: if a or b is not a int or float
    Returns:
        return a + b
    """
    if not isinstance(matrix, list) or\
       not all(isinstance(l, list) for l in matrix) or\
       not all(isinstance(i, (int, float)) for l in matrix for i in l):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not all(len(l) is len(matrix[0]) for l in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return list(map(lambda l: list(map(lambda i: round(i / div, 2), l)), matrix))
