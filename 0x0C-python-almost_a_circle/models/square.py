#!/usr/bin/python3
"""This is a class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class
    Args:
        Rectangle: inheriting Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation of square class by calling Rectangle
        Args:
            size: input size of square
            x: input x
            y: input y
            id: input id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return string of the square information"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """property of size"""
        return self.width

    @size.setter
    def size(self, value):
        """width setter
        Args:
            value: input size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the attributes in the square
        Args:
            args: input arguments
            kwargs: input dictionary
        """
        count = 0
        if args is not None and len(args) != 0:
            for arg in args:
                count += 1
                if count == 1:
                    self.id = arg
                elif count == 2:
                    self.size = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg
        else:
            for key, item in kwargs.items():
                setattr(self, key, item)

    def to_dictionary(self):
        """returns the dictionary representation of square"""
        my_dict = {}
        for a in ["id", "size", 'x', 'y']:
            my_dict[a] = getattr(self, a)
        return my_dict
