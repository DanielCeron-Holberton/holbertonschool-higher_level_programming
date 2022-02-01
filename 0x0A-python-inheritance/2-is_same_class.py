#!/usr/bin/python3
"""This module compares an object with a class"""


def is_same_class(obj, a_class):
    """
    If obj is exactly class returns 
    true else returns false
    """
    if(type(obj) is a_class):
        return True
    else:
        return False
