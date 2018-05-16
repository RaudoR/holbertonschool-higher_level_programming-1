#!/usr/bin/python3
def append_write(filename="", text=""):
    """writes to a file if file exist append
    Args:
        filename: name of the file in string
        text: input string to write
    Return:
        number of charcter writen
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
