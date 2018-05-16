#!/usr/bin/python3
"""class defining student"""


class Student:
    """Base Student class"""
    def __init__(self, first_name, last_name, age):
        """Instantiation of student class
        Args:
            first_name: first name of student
            last_name: last name of student
            age: age of student
        Attributes:
            first_name: public instance first name
            last_name: public instance last name
            age: public instance last name
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """gets the dictionary representation of student
        Args:
            attrs: input attributes in string
        Return:
            dictionary
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict
