#!/usr/bin/python3
"""This class is the base class"""


class Base:
    """Base class for all other modules
    Attributes:
        __nb_objects: private attribute to count objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation of base class
        Args:
            id: input id
        Attributes:
            id: public instance id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
