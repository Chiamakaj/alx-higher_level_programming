#!/usr/bin/python3
"""
A class MyList that inherits from a list
"""


class MyList:
    """
    The MyList Class
    """
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
