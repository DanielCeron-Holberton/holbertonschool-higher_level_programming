#!/usr/bin/python3
"""Base module"""

import json


class Base():
    """Class base structure"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class base structure"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Class base structure"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """Class base structure"""
        list_objs.to_json_string()
