#!/usr/bin/python3
"""Finds the peak"""


def find_peak(list_of_integers):
    """find_peak"""

    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
