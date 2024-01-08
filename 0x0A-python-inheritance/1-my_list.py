#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """print the list, but sorted"""
    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        sort = sorted(self)
        print(sort)
