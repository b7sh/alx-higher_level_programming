#!/usr/bin/python3

"""the square class"""


class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """new square

        size: the size of the square
        position: the posisition of the square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            if not all(isinstance(n, int) for n in value):
                if not all(n >= 0 for n in value):
                    raise TypeError("position must be a \
                            tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """the area"""
        return self.__size * self.__size

    def my_print(self):
        """print in stdout the square with the character #"""
        if self.__size == 0:
            print("")

        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print("")
