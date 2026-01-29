#!/usr/bin/python3
"""
This module defines a Square class with private size and position attributes,
getter and setter for size and position, type/value validation,
and methods to calculate area and print the square with position offset.
"""


class Square:
    """
    This class defines a square with private size and position attributes,
    a public area method, a method to print the square with position,
    and getters/setters for size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position offset (x, y). Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size      # Use setter for validation
        self.position = position  # Use setter for validation

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

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The current position (x, y) of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with type and value validation.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character, with position offset.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        # Print vertical offset (position[1])
        for _ in range(self.__position[1]):
            print()

        # Print each row of the square with horizontal offset (position[0])
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
