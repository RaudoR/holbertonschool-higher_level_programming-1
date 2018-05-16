#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """converts file JSON into obj
    Args:
        filename: name of the file in string
    """
    with open(filename) as f:
        return json.load(f)
