#!/usr/bin/python3
def write_file(filename="", text=""):
    """writes to a file
    Args:
        filename: name of the file in string
        text: input string to write
    Return:
        number of charcter writen
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
