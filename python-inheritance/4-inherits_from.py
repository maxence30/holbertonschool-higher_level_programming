#!/usr/bin/python3
"""Function that checks if an object inherits from a class (but not exact class)."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
