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
        """institation

        Args:
            size (int): size of the square.
        Attributes:
            __size (int): size of square
    """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """size properties"""
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

    def my_print(self):
        """print the square"""
        for y in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print()
