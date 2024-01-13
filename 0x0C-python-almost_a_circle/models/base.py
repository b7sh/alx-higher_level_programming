#!/usr/bin/python3
"""the class base module"""
import json


class Base:
    """Class Base
    This class is the “base” of all other classes in this project
    class constructor: def __init__(self, id=None)
    private class attribute __nb_objects = 0
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization of the Base class
        args:
        id (int): the class id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w') as f:
            if list_objs is None:
                f.wite("[]")
            new_list = [line.to_dictionary() for line in list_objs]
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        representation json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with
        all attributes already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r") as f:
                new_list = cls.from_json_string(f.read())
                return [cls.create(**line) for line in new_list]
        except IOError:
            return []
