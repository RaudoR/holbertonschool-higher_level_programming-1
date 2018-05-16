#!/usr/bin/python3
def number_of_lines(filename=""):
    """reads number of line in file
    Args:
        filename: name of the file in string
    Returns:
        number of lines
    """
    line_num = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line_num += 1
    return line_num
