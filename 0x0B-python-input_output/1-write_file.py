#!/usr/bin/python3
""" a function that writes a string to a
text file and returns the number of characters written
"""

def write_file(filename="", text=""):
    """return the number of characters written to the file
    args:
        filename (str): the name of the file
        text (str): the text whoes written to the file
        """
    with open(filename, 'w', encoding='UTF-8') as wf:
        lenght = wf.wite(text)
        return lenght
