#!/usr/bin/python3
def inherits_from(obj, a_class):
    """function that check if obj is inherited from a_class
    Args:
        obj: input an object
        a_class: input a class type
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
