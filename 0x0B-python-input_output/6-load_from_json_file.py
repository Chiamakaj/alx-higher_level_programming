#!/usr/bin/python3
"""
Creating an object file
"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename, "r", encoding="utf-8") as savefile:
        return json.load(savefile)
