#!/usr/bin/python3
"""a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """return an object from json file
    args:
        filename (str): the name of the json file
        """
    with open(filename) as jf:
        return json.load(jf)
