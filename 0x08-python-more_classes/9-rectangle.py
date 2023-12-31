#!/usr/bin/python3
"""a final class Rectangle that defines a rectangle"""


class Rectangle():
    """represent the rectangle
    artripute:
    number_of_instances
    print_symbol
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width, height):
        """initilization of the rectangle
        args:

        width (int): the width of the rectangle
        height (int): the height of the rectangle
        """
        type(self).number_of_instances += 1
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
        if self.__width == 0 or self.height == 0:
            return ""
        else:
            str_hold = ""
            for i in range(self.__height):
                str_hold += str(self.print_symbol) * self.__width
                if i < self.__height - 1:
                    str_hold += "\n"
            return str_hold

    def __repr__(self):
        """return a string representation of the rectangle"""
        rec = "Rectangle(" + str(self.__width)
        rec += ", " + str(self.__height) + ")"
        return rec

    def __del__(self):
        """Print the message when an instance is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
