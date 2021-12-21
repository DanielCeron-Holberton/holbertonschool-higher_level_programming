#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        ascii_char = ord(str[i])
        if ascii_char > 96 and ascii_char < 123:
            ascii_char -= 32
        if i < len(str) - 1:
            print("{:c}".format(ascii_char), end="")
        else:
            print("{:c}".format(ascii_char))
