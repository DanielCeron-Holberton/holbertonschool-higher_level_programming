#!/usr/bin/python3
def roman_to_int(roman_string):
    if not (isinstance(roman_string, str)):
        return None
    value_integer = []
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
                if value_integer and value_integer[-1] < dict_new.get(key):
                    current_value = dict_new.get(key)
                    value_integer.append(current_value - value_integer[-1])
                    del(value_integer[-2])
                else:
                    current_value = dict_new.get(key)
                    value_integer.append(current_value)

    return sum(value_integer)
