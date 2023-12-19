#!/usr/bin/python3

"""the square class"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """initialize new square

        size: the size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ return the current square area"""
        return self.__size * self.__size
