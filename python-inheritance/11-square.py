#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle
with custom string representation.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle with size validation
    and custom string output.
    """

    def __init__(self, size):
        """Initialize a Square with a given size.

        Args:
            size (int): Size of the square (width and height)
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height
        )
