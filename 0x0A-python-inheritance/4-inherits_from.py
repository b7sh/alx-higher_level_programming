#!/usr/bin/python3
"""a function that returns True if the object is
an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """check if it's an instance from specified class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
