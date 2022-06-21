#!/usr/bin/python3
"""Create a class called square"""


class Square:
    """Define Square Size.

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initializes the square

        Args:
            size (int): size of one side of the square

        Returns:
            None
        """
        self.size = size

    def area(self):
        """Calculates the area of a square

        Return:
            Area of square
        """
        return self.__size ** 2

    def my_print(self):
        """prints square with the character #

        Return:
            Square made of #
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)

    @property
    def size(self):
        """Using getter for size

        Return:
            Size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of square

        Args:
            value (int): the size

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
