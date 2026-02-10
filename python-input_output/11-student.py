#!/usr/bin/python3
"""Module qui définit la classe Student avec serialization et reload.
"""


class Student:
    """Classe qui définit un étudiant avec des méthodes JSON."""

    def __init__(self, first_name, last_name, age):
        """Initialise un étudiant avec prénom, nom et âge."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retourne un dictionnaire représentant l'étudiant.

        Si attrs est une liste de chaînes, seules ces clés sont incluses.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Remplace tous les attributs de l'étudiant avec ceux du dictionnaire."""
        for key, value in json.items():
            setattr(self, key, value)
