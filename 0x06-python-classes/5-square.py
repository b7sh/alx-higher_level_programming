#!/usr/bin/python3

"""the square class"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """intializaiton the square

        size: the size of the square"""
        self.__size = size

    @property
    def size(self):
        """retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an intege")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """find the square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
