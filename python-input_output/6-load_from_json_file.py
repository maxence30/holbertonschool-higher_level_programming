#!/usr/bin/python3
"""Module qui crée un objet Python à partir d'un fichier JSON.
"""
import json


def load_from_json_file(filename):
    """Retourne l'objet Python contenu dans le fichier JSON donné."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
