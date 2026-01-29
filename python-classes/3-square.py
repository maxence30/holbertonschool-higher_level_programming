#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute,
including type and value validation during instantiation, and an area method.
"""


class Square:
    """
    This class defines a square with a private size attribute
    and a public method to calculate its area.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size ** 2
