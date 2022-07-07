#!/usr/bin/python3
"""
A function that reads a text file
"""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it to stdout"""
    with open('filename', mode = "r", encoding = "utf-8") as newfile:
        print(newfile.read(), end="")
