#!/usr/bin/python3

"""the square class"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """a new square initialization

        size: the square size"""
        self.size = size

    @property
    def size(self):
        """retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the value of the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
