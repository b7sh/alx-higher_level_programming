#!/usr/bin/python3
"""a class Rectangle that defines a rectangle"""


class Rectangle():
    """initilization of the rectangle"""

    def __init__(self, width=0, height=0):
        """initialization of the rectangle

        args:

        width (int): the width of the rectangle
        height (int): the height of the rectangle
        """
        self.__width = width
        self.__height = height

        @property
        def width(self):
            """the width value"""
            return self.__width

        @width.setter
        def width(self, value):
            if not value.isdigit():
                raise TypeError("width must be an integer")
            else:
                if value < 0:
                    raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """the height value"""
            return self.__height

        @height.setter
        def height(self, value):
            if not value.isdigit():
                raise TypeError("height must be an integer")
            else:
                if value < 0:
                    raise ValueError("height must be >= 0")
            self.__height = value
