#!/usr/bin/python3
"""Create a class for object square instance"""


class Square:
    """Class for create Square objects"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Getting size attrb"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the value for size attrb"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the area for a Square

        Returns:
            Int: Square area
        """
        return self.size ** 2

    def my_print(self):
        """prints a square
        """
        area = self.area()
        size = self.size
        for i in range(area):
            if i % size == 0 and i != 0:
                print()
            print("#", end="")
        print()
