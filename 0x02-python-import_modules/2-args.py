#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    number_arguments = len(argv[1:])
    arguments = argv[1:]

    if number_arguments == 0:
        print("{} arguments.".format(number_arguments))
    elif number_arguments == 1:
        print("{} argument:".format(number_arguments))
        print("{}: {}".format(number_arguments, arguments[0]))
    else:
        print("{} arguments:".format(number_arguments))
    for arg in range(number_arguments):
        print("{}: {}".format(arg + 1, arguments[arg]))
