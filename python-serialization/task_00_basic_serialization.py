#!/usr/bin/env python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): The data to serialize.
        filename (str): The name of the file to save the JSON data.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file into a Python dictionary.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        dict: The deserialized data.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
