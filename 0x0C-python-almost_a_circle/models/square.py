#!/usr/bin/python3
"""Square Module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square subclass structure"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({s.id}) {s.x}/{s.y} - {s.size}".format(s=self)

    def update(self, *args, **kwargs):
        attr = ["id", "size", "x", "y"]
        i = 0

        for arg in args:
            try:
                setattr(self, attr[i], arg)
                i += 1
            except IndexError:
                return

        for key, value in kwargs.items():
            if key in attr:
                setattr(self, key, value)

    def to_dictionary(self):
        new_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return new_dict
