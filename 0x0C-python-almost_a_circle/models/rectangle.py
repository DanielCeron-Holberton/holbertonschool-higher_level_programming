#!/usr/bin/python3
"""Rectangle module"""


from models.base import Base


class Rectangle(Base):
    """Rectangle subclass structure"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class base structure"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Class base structure"""
        return self.__width

    @width.setter
    def width(self, value):
        """Class base structure"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Class base structure"""
        return self.__height

    @height.setter
    def height(self, value):
        """Class base structure"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Class base structure"""
        return self.__x

    @x.setter
    def x(self, value):
        """Class base structure"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Class base structure"""
        return self.__y

    @y.setter
    def y(self, value):
        """Class base structure"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Class base structure"""
        return self.height * self.width

    def display(self):
        """Class base structure"""
        print("\n" * self.y, end="")
        for i in range(0, self.height):
            print(" " * self.x, end="")
            print("{}".format("#" * self.width))

    def __str__(self):
        """Class base structure"""
        return "[Rectangle] ({s.id}) {s.x}/{s.y} - {s.width}/{s.height}".\
            format(s=self)

    def update(self, *args, **kwargs):
        """Class base structure"""
        attr = ["id", "width", "height", "x", "y"]
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
        """New dictionary"""
        new_dict = {}
        new_dict.update(id=self.id, width=self.width,
                        height=self.height, x=self.x, y=self.y)

        return new_dict
