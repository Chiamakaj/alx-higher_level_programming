#!/usr/bin/python3
"""
A function to write a string
"""


def write_file(filename="", text=""):
    """
    A function that writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as newfile:
        newfile.write(text)
        return len(text)
