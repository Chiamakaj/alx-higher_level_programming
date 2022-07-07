#!/usr/bin/python3
"""
Writing an object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an Object to a text file,
    using a JSON representation
    """
    with open(filename, "w", encoding="utf-8") as jsonfile:
        json.dump(my_obj, jsonfile)
