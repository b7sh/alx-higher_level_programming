#!/usr/bin/python3
"""a function that returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """return the JSON representation
    args:
        my_obj (str): the string
        """
    return json.dumps(my_obj)
