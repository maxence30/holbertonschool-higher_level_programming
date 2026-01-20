#!/usr/bin/python3
"""
Module that provides a function to add two integers.

This module defines a single function that adds two numbers
after validating their types.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats casted to integers.

    Args:
        a (int or float): first number
        b (int or float): second number, defaults to 98

    Raises:
        TypeError: if a or b is not an integer or float

    Returns:
        int: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
