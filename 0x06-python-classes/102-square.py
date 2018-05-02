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
        self.size = size

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
        if type(value) != int and type(value) != float:
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """square the size

        Returns:
            Square of size.
        """
        return self.size ** 2

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __gt__(self, other):
        return self.area() > other.area()
