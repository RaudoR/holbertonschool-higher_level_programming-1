#!/usr/bin/python3
"""class rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """creates base height and width of the rectangle
    Args:
        BaseGeometry: inheriting class BaseGeometry
    """
    def __init__(self, width, height):
        """Instantiation rectaclge with width and height
        Args:
            width: size of width
            height: size of height
        Attributes:
            __width: width of the rectangle
            __height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculate the area of rectangle
        Return:
            area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """return a string of the area funciton
        Return:
            returns a string
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
