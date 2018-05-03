#!/usr/bin/python3
"""
This module does simple addition
"""


def add_integer(a, b=98):
    """
    Simple addition function that adds 2 integers or float
    first it checks if 2 given input is an integer or a float
    than converts float to integers
    Args:
        a: input variable
        b: input variable default to 98 if none
    Raises:
        TypeError: if a or b is not a int or float
    Returns:
        return a + b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
