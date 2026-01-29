#!/usr/bin/python3
"""
9-rectangle.py: Définit la classe Rectangle.

Classe Rectangle avec :
- Attributs privés width et height
- Attributs de classe number_of_instances et print_symbol
- Méthodes instance : area, perimeter, __str__, __repr__, __del__
- Méthodes statiques : bigger_or_equal
- Méthode de classe : square
"""

class Rectangle:
    """Classe Rectangle avec méthodes avancées et suivi d'instances."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retourne l'aire du rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Retourne le périmètre du rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Affiche le rectangle avec le symbole print_symbol."""
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join([symbol * self.width for _ in range(self.height)])

    def __repr__(self):
        """Retourne une chaîne pour recréer une instance via eval()."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Affiche un message à la suppression et décrémente number_of_instances."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Retourne le rectangle ayant la plus grande aire."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Retourne un nouveau Rectangle carré (width = height = size)."""
        return cls(size, size)
