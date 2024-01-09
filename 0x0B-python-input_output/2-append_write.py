#!/usr/bin/python3
"""a function that appends a string
at the end of a text file"""


def append_write(filename="", text=""):
    """append the string at the end of the file
    and return the lenghth of the string
    args:
    filename (str): the name of the file
    text (str): the text to be written
    """
    with open(filename, 'a+', encoding='UTF-8') as af:
        return af.write(text)
