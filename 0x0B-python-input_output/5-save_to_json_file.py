#!/usr/bin/python3
"""Defines a JSON file function."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to text file."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
