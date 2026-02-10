#!/usr/bin/python3
"""Module qui retourne le dictionnaire d'attributs simples d'un objet.
"""


def class_to_json(obj):
    """Retourne un dictionnaire contenant tous les attributs simples
    (list, dict, str, int, bool) de l'objet donné.
    """
    return obj.__dict__.copy()
