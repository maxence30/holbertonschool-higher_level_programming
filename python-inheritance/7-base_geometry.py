#!/usr/bin/python3
"""Module that defines a BaseGeometry class with area and integer validation."""


class BaseGeometry:
    """BaseGeometry class with an unimplemented area method and integer validator."""

    def area(self):
        """Raises an Exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer.

        Args:
            name (str): Name of the parameter
            value (int): Value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
