#!/usr/bin/python3
"""Appends text to file"""


def append_write(filename="", text=""):
    """Appends text to file with open function"""

    with open(filename, "a") as f:
        my_file = f.write(text)
        f.close()
        return my_file
