#!/usr/bin/python3
def lookup(obj):
    """this function returns the list of available attributes and method
    Args:
        obj: input class object
    """
    return list(i for i in dir(obj))
