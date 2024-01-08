#!/usr/bin/python3
"""a class BaseGeometry"""


class BaseGeometry:
    """representing the BaseGeometry"""
    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """vale parameter is an integer
        args:

        name (str): string
        value (int): always integer
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
