#!/usr/bin/python3
"""Rectangle class that inherits from base"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from base
    Private instance attributes,
    each with its own public getter and setter:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization of the Rectangle class
        args:
        width (int): the width of the class
        height (int): the height of the class
        x (int): the x cordinate
        y (int): the y cordinate
        id (id): the id of the class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """the value of the x cordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """the value of the y cordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """the value of the area"""
        return self.width * self.height

    def display(self):
        """display the Rectangle instance
        with the character #
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y_axis in range(self.y)]
        for row in range(self.height):
            [print(" ", end="") for x_axis in range(self.x)]
            for column in range(self.width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """update the attributes
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """
        names = ["id", "width", "height", "x", "y"]
        for key, value in zip(names, args):
            setattr(self, key, value)
        for key, value in kwargs.items():
            if key in names:
                setattr(self, key, value)

    def to_dictionary(self):
        """the dictionary representing ro Rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y}

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(
                Rectangle.__name__, self.id, self.x, self.y,
                self.width, self.height)
