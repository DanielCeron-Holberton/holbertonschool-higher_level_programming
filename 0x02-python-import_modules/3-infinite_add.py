#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arguments = argv[1:]
    int_arguments = 0

    for a in range(len(arguments)):
        int_arguments += int(arguments[a])
    print(int_arguments)
