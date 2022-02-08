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

    @classmethod
    def save_to_file(cls, list_objs):
        """Class base structure"""
        file_name = "{}.json".format(cls.__name__)
        list_file = []

        if list_objs:
            for obj in list_objs:
                list_file.append(cls.to_dictionary(obj))
        with open(file_name, "w") as f:
            f.write(cls.to_json_string(list_file))

    @staticmethod
    def from_json_string(json_string):
        """Class base structure"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class base structure"""

        if cls.__name__ == "Square":
            poor_dummy = cls(1)
        else:
            poor_dummy = cls(1, 1)
        poor_dummy.update(**dictionary)
        return poor_dummy

    @classmethod
    def load_from_file(cls):
        """Class base structure"""

        file_name = "{}.json".format(cls.__name__)
        new_list = []
        try:
            with open(file_name, "r") as f:
                json_object = cls.from_json_string(f.read())

            for import_class in json_object:
                new_list.append(cls.create(**import_class))
            return new_list

        except (FileNotFoundError, TypeError):
            return []
