#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """JSON representaiton of my_obj
    Args:
        my_obj: input any object
    Return:
        return JSON representation of string
    """
    return json.dumps(my_obj)
