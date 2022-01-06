#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dictionary = a_dictionary.copy()
    for key in new_dictionary:
        if value == new_dictionary.get(key):
            a_dictionary.pop(key, None)

    return a_dictionary
