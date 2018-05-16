#!/usr/bin/python3
import json


def from_json_string(my_str):
    """convert JSON string to object
    Args:
        my_str: input string representation of obj
    Return:
        return object
    """
    return json.loads(my_str)
