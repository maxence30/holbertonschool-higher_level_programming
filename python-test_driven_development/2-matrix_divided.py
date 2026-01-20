#!/usr/bin/python3
"""
Module that provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number.

    Args:
        matrix (list of lists of int/float): the matrix to divide
        div (int or float): the divisor

    Raises:
        TypeError: if matrix elements are not int/float, or rows not same size, or div is not a number
        ZeroDivisionError: if div is 0

    Returns:
        list of lists of float: new matrix with elements divided and rounded to 2 decimals
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)
    return new_matrix
