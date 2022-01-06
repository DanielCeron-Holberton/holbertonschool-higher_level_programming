#!/usr/bin/python3
def roman_to_int(roman_string):
    if not (isinstance(roman_string, str)):
        return None
    value_integer = 0
    dict_new = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    for letter in roman_string:
        for key in dict_new:
            if letter == key:
                if value_integer != 0 and value_integer < dict_new.get(key):
                    value_integer = dict_new.get(key) - value_integer
                else:
                    value_integer += dict_new.get(key)

    return value_integer
