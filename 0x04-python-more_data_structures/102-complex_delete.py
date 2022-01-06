#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not value:
        return a_dictionary
    new_dictionary = {}
    for element in a_dictionary:
        current = a_dictionary.get(element)
        if current != value:
            new_dictionary.update({element: current})
        else:
            continue
    return new_dictionary
