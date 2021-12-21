#!/usr/bin/python3


def remove_char_at(str, n):
    new_string = ""
    for i in range(len(str)):
        if n != i:
            new_string += str[i]
    return (new_string)
