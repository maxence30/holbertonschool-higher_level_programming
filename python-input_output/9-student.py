#!/usr/bin/python3
"""Module qui définit la classe Student avec méthode to_json.
"""


class Student:
    """Classe qui définit un étudiant."""

    def __init__(self, first_name, last_name, age):
        """Initialise un étudiant avec son prénom, nom et âge."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retourne un dictionnaire représentant l'étudiant."""
        return self.__dict__.copy()
