#!/usr/bin/python3
"""Module qui retourne l'objet Python représenté par une chaîne JSON.
"""
import json


def from_json_string(my_str):
    """Retourne l'objet Python correspondant à la chaîne JSON donnée."""
    return json.loads(my_str)
