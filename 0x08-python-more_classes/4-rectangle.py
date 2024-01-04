#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle():
    """operating the rectangle"""
    def __init__(self, width, height):
        """initilization of the rectangle
        args:

        width (int): the width
        height (int): the height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """the area value"""
        return (self.__width * self.__height)

    def perimeter(self):
        """the perimeter value"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            hold_str = ""
            for i in range(self.__height):
                hold_str += "#" * self.__width
                if i < self.__height - 1:
                    hold_str += "\n"
                return hold_str

    def __repr__(self):
        """
        return a string representation of the rectangle
        to be able to recreate a new instance
        """
        width_height = "(Rectangle" + str(self__width)
        width_height += ", " + str(self.__height) + ")"
        return width_height
