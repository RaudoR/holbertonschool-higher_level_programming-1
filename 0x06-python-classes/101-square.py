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
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """position setter

        Note:
            Do not include the `self` parameter in the ``Args`` section.
        Args:
            value (tuple): position
        Attributes:
            __position (tuple): position
        """
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not(type(value[0]) is int and type(value[1]) is int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """square the size

        Returns:
            Square of size.
        """
        return self.size ** 2

    def my_print(self):
        """print the square in the cordinates"""
        if self.size == 0:
            print()
            return
        for j in range(self.position[1]):
            print()
        for i in range(self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))

    def __str__(self):
        if self.size == 0:
            return ""
        str1 = ""
        for j in range(self.position[1]):
            str1 += '\n'
        for y in range(self.size):
            for i in range(self.position[0]):
                str1 += ' '
            for x in range(self.size):
                str1 += '#'
            if y < self.size - 1:
                str1 += '\n'
        return str1
