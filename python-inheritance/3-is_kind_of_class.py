#!/usr/bin/python3
"""
Function that checks if an object is an instance of a class or
an instance of a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class or of a subclass of it.
    """
    return isinstance(obj, a_class)
