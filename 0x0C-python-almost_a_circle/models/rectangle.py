#!/usr/bin/python3
"""This is a class rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class
    Args:
        Base: inheriting Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation of rectangel class
        Args:
            width: input width of the rectangle
            height: input height of the rectangle
            x: input x
            y: input y
            id: input id
        Attributes:
            width: instance attribute for width
            height: instance attribute for height
            x: instance attribute for x
            y: instance attribute for y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """property of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        Args:
            value: size of width
        Attributes:
            __width: private instance attribute for width
        """
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """property of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        Args:
            value: size of height
        Attributes:
            __height: private instance attribute for height
        """
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """property of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter
        Args:
            value: size of x
        Attributes:
            __x: private instance attribute for x
        """
        self.integer_validator('x', value)
        self.__x = value

    @property
    def y(self):
        """property of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter
        Args:
            value: size of y
        Attributes:
            __y: private instance attribute for y
        """
        self.integer_validator('y', value)
        self.__y = value

    def integer_validator(self, name, value):
        """method to check if its an integer
        Args:
            name: input name
            value: input integer
        Raises:
            TypeError: when value is not an int
            ValueError: when name is width or height and
                        value is less than or equal to 0
            ValueError: when name is x or y
                        value is less than 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError("{:s} must be > 0".format(name))
        if (name == 'x' or name == 'y') and value < 0:
            raise ValueError("{:s} must be >= 0".format(name))

    def area(self):
        """gets the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """print the square"""
        result = "" + ' ' * self.x
        result = result + str('#') * self.width
        result = '\n' * self.y + '\n'.join(
            list(result for i in range(self.height)))
        print(result)

    def __str__(self):
        """return string of the rectangle information"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update the attributes in the rectangle
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
                    self.width = arg
                elif count == 3:
                    self.height = arg
                elif count == 4:
                    self.x = arg
                elif count == 5:
                    self.y = arg
        else:
            for key, item in kwargs.items():
                setattr(self, key, item)

    def to_dictionary(self):
        """returns the dictionary representation of rectangle"""
        my_dict = {}
        for a in ["id", "width", "height", 'x', 'y']:
            my_dict[a] = getattr(self, a)
        return my_dict
