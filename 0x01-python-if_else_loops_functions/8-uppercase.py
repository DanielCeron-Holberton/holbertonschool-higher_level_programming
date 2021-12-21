#!/usr/bin/python3
def uppercase(str):
    new_string = ""
    for i in str:
        ascii_char = ord(str[i])
        if ascii_char > 96 and ascii_char < 123:
            new_string += chr(ascii_char - 32)
        else:
            new_string += str[i]
    print(new_string)