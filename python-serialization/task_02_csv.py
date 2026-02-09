#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(filename):
    """
    Convert a CSV file to JSON and save it to data.json.

    Args:
        filename (str): The CSV file to convert.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file)

        return True
    except (FileNotFoundError, OSError, csv.Error):
        return False
