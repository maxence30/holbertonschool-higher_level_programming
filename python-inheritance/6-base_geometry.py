#!/usr/bin/python3
"""BaseGeometry class with an unimplemented area method."""


class BaseGeometry:
    """BaseGeometry class with an area() method not implemented."""

    def area(self):
        """Raise an Exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")
