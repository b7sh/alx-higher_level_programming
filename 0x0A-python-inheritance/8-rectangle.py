#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initialization of the Rectangle
        args:

        width (int): the width
        height (int): the height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
