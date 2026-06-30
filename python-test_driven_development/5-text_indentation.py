#!/usr/bin/python3
"""
Module that provides a function to print text with 2 new lines
after each '.', '?', or ':' character.
"""


def text_indentation(text):
    """
    Print text with 2 new lines after '.', '?', or ':'.

    Args:
        text (str): the text to print

    Raises:
        TypeError: if text is not a string

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    end_chars = ".?:"
    i = 0
    length = len(text)

    while i < length:
        line = ""
        while i < length and text[i] not in end_chars:
            line += text[i]
            i += 1
        if i < length and text[i] in end_chars:
            line += text[i]
            i += 1
        print(line.strip())
        if i < length and text[i-1] in end_chars:
            print()
