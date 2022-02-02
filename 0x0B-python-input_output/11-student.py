#!/usr/bin/python3
"""Creates a student class"""


class Student ():
    """Creates a student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        new_dict = {}

        if attrs is None:
            return self.__dict__

        for attr in attrs:
            if attr in self.__dict__.keys():
                new_dict[attr] = self.__dict__[attr]

        return new_dict

    def reload_from_json(self, json):

        for key, value in json.items():
            setattr(self, key, value)
