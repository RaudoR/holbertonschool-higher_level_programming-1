#!/usr/bin/python3
def read_file(filename=""):
    """reads file inputed
    Args:
        filename: name of the file in string
    """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
