#!/usr/bin/python3
""" a function that inserts a line of
text to a file, after each line
containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """insert the line after each specific string
    args:
    filename (str): the name of the file
    search_string (str): the specific character
    new_string (str): the string to insert
    """
    new_text = ""
    with open(filename) as rf:
        for line in rf:
            new_text += line
            if search_string in line:
                new_text += new_string
    with open(filename, 'w') as wf:
        wf.write(new_text)
