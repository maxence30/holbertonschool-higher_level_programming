#!/usr/bin/python3
"""Module qui lit un fichier texte UTF-8 et l'affiche sur la sortie standard."""

def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
