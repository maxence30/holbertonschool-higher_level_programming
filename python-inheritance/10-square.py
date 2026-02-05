#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle with size validation."""

    def __init__(self, size):
        """Initialize a Square with a given size.

        Args:
            size (int): Size of the square (width and height)
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
