#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    values_list = sorted(list(a_dictionary.values()))
    bigger_value = values_list[-1]
    for key in a_dictionary:
        value_dict = a_dictionary.get(key)
        if value_dict == bigger_value:
            print(key)
            return key
