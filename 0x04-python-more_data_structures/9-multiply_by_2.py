#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key in a_dictionary:
        value_dict = a_dictionary.get(key) * 2
        new_dictionary.update({key: value_dict})
    return new_dictionary
