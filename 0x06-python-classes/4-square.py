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
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """size setter

        Note:
            Do not include the `self` parameter in the ``Args`` section.
        Args:
            value (int): size of the square.
        Attributes:
            __size (int): size of square
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """square the size

        Returns:
            Square of size.
        """
        return self.__size ** 2
