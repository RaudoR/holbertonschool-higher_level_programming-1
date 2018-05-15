#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """function that check if obj is kind of a_class
    Args:
        obj: input an object
        a_class: input a class type
    """
    if isinstance(obj, a_class):
        return True
    return False
