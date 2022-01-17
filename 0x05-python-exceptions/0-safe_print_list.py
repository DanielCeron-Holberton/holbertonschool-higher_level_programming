#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    i = 0
    while x:
        try:
            print(my_list[i], end='')
            i += 1
            if x == 1:
                print()
            x -= 1
        except IndexError:
            print()
            break
    return i
