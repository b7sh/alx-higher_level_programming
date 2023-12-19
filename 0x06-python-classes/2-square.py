#!/usr/bin/python3

"""class to the square"""


class Square:
    """the square representiation"""
    def __init__(self, size=0):
        """the new square

        size: the size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
