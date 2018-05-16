#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """write to a file with json representation
    Args:
        my_obj: input object
        filename: name of the file in string
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
