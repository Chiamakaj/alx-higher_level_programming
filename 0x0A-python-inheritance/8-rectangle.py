#!/usr/bin/python3
"""
A class Rectangle that inherits from
BaseGeometry SuperClass.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initializes the class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
