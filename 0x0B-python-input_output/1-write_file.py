#!/usr/bin/python3
"""
A function to write a string
"""


def write_file(filename="", text=""):
    """
    A function that writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, mode = "w", encoding = "utf-8") as newfile:
        i = 0
        for word in newfile:
            for char in word:
                i += 1
        return i
