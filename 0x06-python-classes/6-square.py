#!/usr/bin/python3
"""Create a class for object square instance"""


class Square:
    """Class for create Square objects"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (len(value) == 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if(value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(value[0], int) or isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value



    def area(self):
        """Computes the area for a Square

        Returns:
            Int: Square area
        """
        return self.size ** 2

    def my_print(self):
        """prints a square
        """
        area=self.area()
        size=self.size
        position1 = self.position[0]
        position2 = self.position[1]
        if size != 0:
            while position2:
                print()
                position2 -= 1
        for i in range(area):
            position1 = self.position[0]
            if i % size == 0:
                if i != 0:
                    print()
                while position1:
                    print(" ", end="")
                    position1 -= 1
            print("#", end="")
        print()
