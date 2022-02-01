#!/usr/bin/python3
"""Module that creates a list subclass"""


class MyList(list):
    """Creates a subclass"""

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        my_new_list = self.copy()
        my_new_list.sort()
        print(my_new_list)
