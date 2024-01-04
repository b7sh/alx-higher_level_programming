#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle():
    """represent the rectangle"""
    def __init__(self, width=0, height=0):
        """initilization of the rectangle
        args:

        width (int): the width of the rectangle
        heught (int): the height of the rectangle
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
        """print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            str_hold
            for i in range(self.__height):
                str_hold += "#" * self.__width
                if i < self.__height -1:
                    str_hold += "\n"
            return str_hold

    def __repr__(self):
        """ return a string representation of the rectangle"""
        rec = "Rectangle(" + str(self.__width)
        rec += ", " + str(self.__height) + ")"
        return rec

    def __del__(self):
        """Print the message when an instance is deleted"""
        print("Bye rectangle...")
