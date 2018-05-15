#!/usr/bin/python3
"""This class inherits from list"""


class MyList(list):
    """inherits list class
    Args:
        list: inheriting class list
    """
    def print_sorted(self):
        print(sorted(self))
