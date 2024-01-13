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
                Square.__name__, self.id, self.x, self.y, self.width)

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
        if args and len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif index == 1:
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
                index += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """return dictionary of square class"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y}
