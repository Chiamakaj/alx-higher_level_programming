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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if attrs == None or type(attrs) != list:
            return self.__dict__
        else:
            temp = {}
            for elem in attrs:
                if type(elem) != str:
                    return self.__dict__
                if elem in self.__dict__.keys():
                    emp[elem] = self.__dict__[elem]
            return temp

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for items in json.keys():
            self.__dict__[items] = json[items]
