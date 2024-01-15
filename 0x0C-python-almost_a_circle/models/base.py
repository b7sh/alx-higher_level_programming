#!/usr/bin/python3
"""the class base module"""
import json
import csv
import turtle


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
        """save the json string to file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w', encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                json_list = [line.to_dictionary() for line in list_objs]
                f.write(Base.to_json_string(json_list))

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
        file_name = "{}.json".format(cls.__name__)
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                new_list = Base.from_json_string(f.read())
                return [cls.create(**line) for line in new_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """write to csv file"""
        file_name = "{}.csv".format(cls.__name__)
        with open(file_name, "w", newline="") as f:
            writer = csv.writer(f)
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow([
                            obj.id, obj.width, obj.height, obj.x, obj.y])
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        file_name = "{}.csv".format(cls.__name__)
        instances = []
        try:
            with open(file_name, "r", newline="") as f:
                reader = csv.reader(f)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(
                                int(row[1]), int(
                                    row[2]), int(
                                        row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        instance = cls(
                                int(row[1]), int(
                                    row[2]), int(row[3]), int(row[0]))
                    instances.append(instance)
        except FileNotFoundError:
            pass
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        mul = turtle.Turtle()
        wn = turtle.Screen()
        turtle.colormode(255)
        wn.bgcolor(170, 30, 20)
        mul.shape("turtle")
        mul.pensize(4)
        mul.color("brown")

        for rad in list_rectangle:
            mul.showturtle()
            mul.up()
            mul.goto(rad.x, rad.y)
            mul.down()
            for x in range(2):
                mul.forward(rad.width)
                mul.left(90)
                mul.forward(rad.height)
                mul.left(90)
                mul.home()

        mul.color("green")
        for rad in list_squares:
            mul.showturtle()
            mul.up()
            mul.goto(rad.x, rad.y)
            mul.down()
            for x in range(4):
                mul.forward(rad.size)
                mul.left(90)
                mul.home()

        turtle.exitonclick()
