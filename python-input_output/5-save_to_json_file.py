#!/usr/bin/python3
"""Module qui écrit un objet Python dans un fichier texte en JSON.
"""
import json


def save_to_json_file(my_obj, filename):
    """Écrit l'objet Python dans le fichier en utilisant JSON."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
