#!/usr/bin/python3
"""a function that reads a text file and print it to the stdout"""


def read_file(filename=""):
    """print the content of the file"""
    with open(filename, 'r', encoding='UTF-8') as rf:
        for line in rf:
            print(line, end="")
