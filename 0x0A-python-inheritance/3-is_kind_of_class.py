#!/usr/bin/python3
"""a function that returns True if the object is
an instance of, or if the object is an instance
of a class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """check if it's instance of a_class"""
    if isinstance(obj, a_class):
        return True
    return False
