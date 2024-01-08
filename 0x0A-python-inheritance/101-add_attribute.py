#!/usr/bin/python3
"""a function that adds a new attribute to an object"""


def add_attribute(obj, attr, value):
    """adds new attributes
    args:
    abj (any): the object
    attr (str): the attribute
    value (int): the value
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
