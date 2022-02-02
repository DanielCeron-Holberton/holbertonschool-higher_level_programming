#!/usr/bin/python3
"""Writes a file"""


def write_file(filename="", text=""):
    """Writes a file with open function"""

    with open(filename, "w") as f:
        my_file = f.write(text)
        f.close()
        return my_file
