#!/usr/bin/python3
"""class geometry module"""


class BaseGeometry:
    """Base geometry class"""
    def area(self):
        """area method that has nothing
        Raises:
            Excpetion: are is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method to check if its an integer
        Args:
            name: input name
            value: input integer
        Raises:
            TypeError: when value is not an int
            ValueError: when value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
