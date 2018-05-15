#!/usr/bin/python3
"""class square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """creates base size square
    Args:
        BaseGeometry: inheriting class BaseGeometry
    """
    def __init__(self, size):
        """Instantiation sqaure with size
        Args:
            size: size of square
        Attributes:
            __size: size of the rectangle
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """return a string of the area funciton
        Return:
            returns a string
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
