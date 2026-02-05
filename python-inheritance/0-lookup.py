#!/usr/bin/python3
"""Module that lists available attributes and methods of an object."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return dir(obj)
