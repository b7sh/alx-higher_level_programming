#!/usr/bin/python3
"""a function that checks if the object is an instance"""


def is_same_class(obj, a_class):
    """check if it's an instance
    returns:
        True: if it's an instance
        False: if it's not
        """
    if isinstance(obj, a_class):
        return True
    return False
