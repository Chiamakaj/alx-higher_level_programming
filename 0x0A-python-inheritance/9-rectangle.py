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

    def area(self):
        """calculate area"""
        return self.__width * self.__height

    def __str__(self):
        """Magic methos for rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
