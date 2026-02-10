#!/usr/bin/python3
"""Module qui ajoute une chaîne de caractères à la fin d'un fichier texte UTF-8.
"""


def append_write(filename="", text=""):
    """Ajoute du texte à la fin d'un fichier UTF-8 et retourne le nombre
    de caractères ajoutés.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
