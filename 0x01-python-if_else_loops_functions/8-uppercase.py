#!/usr/bin/python3
def uppercase(str):
    for i in str:
        ascii_char = ord(i)
        if ascii_char > 96 and ascii_char < 123:
            new_string = chr(ascii_char - 32)
        else:
            new_string = i
        print("{}".format(new_string), end="")
    print("")
