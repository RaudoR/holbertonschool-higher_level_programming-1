#!/usr/bin/python3
"""
This module prints text with indentation
"""


def text_indentation(text):
    """
    prints indentation when there is a . ? or :
    Args:
        text: input string
    Raises:
        TypeError: check if text is a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace('.', '.\n')
    text = text.replace('?', '?\n')
    text = text.replace(':', ':\n')
    print("\n\n".join(list(l.strip() for l in text.split('\n'))), end="")
