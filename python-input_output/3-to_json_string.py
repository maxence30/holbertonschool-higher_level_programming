#!/usr/bin/python3
"""Module qui retourne la représentation JSON d'un objet Python.
"""
import json


def to_json_string(my_obj):
    """Retourne la chaîne JSON correspondant à l'objet Python donné."""
    return json.dumps(my_obj)
