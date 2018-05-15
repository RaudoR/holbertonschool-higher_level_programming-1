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
