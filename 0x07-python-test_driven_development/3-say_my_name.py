#!/usr/bin/python3
"""
This module prints out the name
"""


def say_my_name(first_name, last_name=""):
    """
    prints name
    Args:
        first_name: input string
        last_name: input string and empty when its None
    Raises:
        TypeError: if both name is not string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
