#!/usr/bin/python3
class Square:
    """class square

    Note:
        Do not include the `self` parameter in the ``Args`` section.
    Args:
        size (int): size of the square.
    Attributes:
        __size (int): size of square
    """
    def __init__(self, size=0):
        """instiitation

        Args:
            size (int): size of the square.
        Attributes:
            __size (int): size of square
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) != int:
            raise TypeError("size must be an integer")
        self.__size = size
