#!/usr/bin/python3

"""Creates a pascal triangle"""


def pascal_triangle(n):
    """return pascal triangle"""

    list = []  # an empty list

    for n in range(n):
        list.append([])
        list[n].append(1)
        for m in range(1, n):
            list[n].append(list[n - 1][m - 1] + list[n - 1][m])
        if(n != 0):
            list[n].append(1)

    return list
