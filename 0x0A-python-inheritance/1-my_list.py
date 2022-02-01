#!/usr/bin/python3


class MyList(list):

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        my_new_list = self.copy()
        my_new_list.sort()
        print(my_new_list)
