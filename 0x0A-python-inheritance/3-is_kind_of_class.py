#!/usr/bin/python3
"""This module return if is a class or a subclass"""


def is_kind_of_class(obj, a_class):
    """True if is class or subclass
    else returns false"""
    if(isinstance(obj, a_class)):
        return True
    else:
        return False
