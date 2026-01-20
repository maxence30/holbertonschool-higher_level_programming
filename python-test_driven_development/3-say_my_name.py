#!/usr/bin/python3
"""
Module that provides a function to print a full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Print 'My name is <first_name> <last_name>'.

    Args:
        first_name (str): first name
        last_name (str): last name, defaults to empty string

    Raises:
        TypeError: if first_name or last_name is not a string

    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}".rstrip())
