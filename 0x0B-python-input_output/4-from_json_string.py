#!/usr/bin/python3
"""a function that returns an object
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """return an object represent by json string
    args:
    my_str (string): the string to return
    """
    return json.loads(my_str)
