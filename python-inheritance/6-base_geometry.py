#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an unimplemented area method."""


class BaseGeometry:
    """BaseGeometry class with an area method not implemented."""

    def area(self):
        """Raises an Exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")
