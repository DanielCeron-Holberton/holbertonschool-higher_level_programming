#!/usr/bin/python3
""""""

from turtle import width
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value


    def __str__(self):
        return "[Square] ({s.id}) {s.x}/{s.y} - {s.size}".format(s=self)
    def update(self, *args, **kwargs):
        attr = ["id", "size", "x", "y"]
        i = 0
        for arg in args:
            if hasattr(self, arg):
                setattr(self, attr[i], arg)
            i += 1
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
