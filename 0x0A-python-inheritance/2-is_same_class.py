#!/usr/bin/python3
def is_same_class(obj, a_class):
    """funciton to figure if the obj is exactly the class
    Args:
        obj: input an object
        a_class: input a class type
    """
    if type(obj) is a_class:
        return True
    return False
