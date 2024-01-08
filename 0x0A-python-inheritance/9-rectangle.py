#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from the bassegeometry class"""
    def __init__(self, width, height):
        """initializaion of the Rectangle class
        args:

        width (int): the width
        height (int): the height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        str_name = "[" + str(self.__class__.__name__) + "]"
        str_name += str(self.__width) + "/" + str(self.++height)
