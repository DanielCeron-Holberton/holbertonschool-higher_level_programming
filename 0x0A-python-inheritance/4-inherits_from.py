#!/usr/bin/python3
"""This module return if only is a subclass"""


def inherits_from(obj, a_class):
    """True if is subclass
    otherwise returns false"""
    if(isinstance(obj, a_class) and type(obj) is not a_class):
        return True
    else:
        return False
