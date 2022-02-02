#!/usr/bin/python3
"""Read from a file"""


def read_file(filename=""):
    """Read from file with open function"""

    with open(filename) as f:
        read_data = f.read()
        print(read_data, end="")
