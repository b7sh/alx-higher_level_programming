#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:
    """representing the class"""
    def __init__(self, first_name, last_name, age):
        """initialization of the Student class
        args:

        first_name (str): the student first name
        last_name (str): the student last name
        age (int): the student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
