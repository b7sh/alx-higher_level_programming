#!/usr/bin/python3
""" a function that writes an Object to a text file
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """wite an object using json to a text file
    args:
    my_object (str): the string
    filename (str): the file name
    """
    with open(filename, 'w') as jf:
        jf.write(json.dumps(my_obj))
