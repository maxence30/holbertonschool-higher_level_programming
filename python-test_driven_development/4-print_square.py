#!/usr/bin/python3
"""
Module that provides a function to print a square with the character #.
"""


def print_square(size):
    """
    Print a square of size 'size' using the '#' character.

    Args:
        size (int): the size of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
