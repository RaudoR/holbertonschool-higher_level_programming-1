#!/usr/bin/python3
def class_to_json(obj):
    """returns the dictionary description with simple data structure
    Args:
        obj: instance of a Class
    Returns:
        dictionary descripitoin of simple structure
    """
    return vars(obj)
