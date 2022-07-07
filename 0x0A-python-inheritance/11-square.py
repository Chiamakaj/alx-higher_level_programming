#!/usr/bin/python3
"""
A class Square that inherits from
Rectangle subclass.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class"""
    def __init__(self, size):
        """Instantiate the class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """method to get the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """Method to describe the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
