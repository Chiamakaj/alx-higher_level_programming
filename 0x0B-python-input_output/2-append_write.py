#!/usr/bin/python3
"""
Appending a string
"""


def append_write(filename="", text=""):
    """
    A function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as newadd:
        newadd.write(text)
        return len(text)
