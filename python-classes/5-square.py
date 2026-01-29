#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute,
getter and setter for size, type/value validation, and methods
to calculate area and print the square.
"""


class Square:
    """
    This class defines a square with a private size attribute,
    a public area method, a method to print the square,
    and getter/setter for size.
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
        self.size = size  # Use setter for validation

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with type and value validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print('#' * self.__size)
