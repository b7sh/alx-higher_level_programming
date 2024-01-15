#!/usr/bin/python3
from models.rectangle import Rectangle
"""class Square that inherits from Rectangle"""


class Square(Rectangle):
    """representing square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialization of the square class
        args:
        size (int): the size of the square
        x (int): the a_axis
        y (int): the y_axis
        id (int): the id o the class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return the presentation of the square"""
        return "[{}] ({}) {}/{} - {}".format(
                Square.__name__, self.id, self.x, self.y, self.size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the class
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        """
        names = ["id", "size", "x", "y"]
        for key, value in zip(names, args):
            setattr(self, key, value)
        for key, value in kwargs.items():
            if key in names:
                setattr(self, key, value)

    def to_dictionary(self):
        """return dictionary of square class"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y}
