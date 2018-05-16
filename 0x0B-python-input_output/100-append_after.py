#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """writes to a file
    Args:
        filename: name of the file in string
        search_string: input string to search
        new_string: input string to write
    """
    with open(filename, 'r', encoding='utf-8') as f:
        tmp = f.readlines()
    with open(filename, 'w', encoding='utf-8') as f:
        for line in tmp:
            if search_string in line:
                line = line + new_string
            f.write(line)
