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
        self._width = width
        self._height = height

        @property
        def width(self):
            """the width value"""
            return self._width

        @width.setter
        def width(self, value):
            if not self._width.isdigit():
                raise TypeError("width must be an integer")
            else:
                if self._width < 0:
                    raise ValueError("width must be >= 0")

        @property
        def height(self):
            """the height value"""
            return self.height

        @height.setter
        def height(self, value):
            if not self.height.isdigit():
                raise TypeError("height must be an integer")
            else:
                if self.height < 0:
                    raise ValueError("height must be >= 0")
