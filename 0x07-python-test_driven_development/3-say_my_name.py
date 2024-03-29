#!/usr/bin/python3
""" a function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """print the first and the last name
    args:
    first_name (str): the first name
    lat_name (str): the last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("my name is {} {}".format(first_name, last_name))
