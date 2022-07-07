#!/usr/bin/python3
"""
A class BaseGeometry
"""


class BaseGeometry:
    """An empty class"""
    def __init__(self):
        """Initializes the class"""
        pass
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
