#!/usr/bin/python3
def no_c(my_string):
    i = 0
    new_string = ""
    for letter in my_string:
        if letter == "c" or letter == "C":
            continue
        else:
            new_string += letter
    return new_string
