#!/usr/bin/python3
"""my int class"""


class MyInt(int):
    """creates MyInt class
    Args:
        int: inheriting class int
    """
    def __init__(self, value):
        """Instantiation sqaure with size
        Args:
            value: input integer
        Attributes:
            __integer: integer inputed
        """
        self.__integer = value

    def __eq__(self, num):
        """check if its equal
        Args:
            num: input integer
        Return:
            false if its equal
        """
        return self.__integer != num

    def __ne__(self, num):
        """check if its not equal
        Args:
            num: input integer
        Return:
            false if its not equal
        """
        return self.__integer == num

    def __str__(self):
        """returns a string
        Return:
            string of the number
        """
        return str(self.__integer)
