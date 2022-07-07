#!/usr/bin/python3
"""
Writing from json
"""


def from_json_string(my_str):
    """
    A function that returns an object (Python data structure)
    represented by a JSON string
    """
    import json
    return json.loads(my_str)
