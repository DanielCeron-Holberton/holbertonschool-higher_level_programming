#!/usr/bin/python3



BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        super().__init__()
        if(self.integer_validator("width", width) == True):
            self.__width = width
        if(self.integer_validator("height", height) == True):
            self.__height = height
