#!/usr/bin/python3
"""
A function that returns Boolean
"""


def is_kind_of_class(obj, a_class):
    """defines the object"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
