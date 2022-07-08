#!/usr/bin/python3
"""
A class called student
"""


class Student:
    """A class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student"""
        return self.__dict__
