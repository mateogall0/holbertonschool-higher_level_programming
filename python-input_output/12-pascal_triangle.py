#!/usr/bin/python3
"""Module"""


def pascal_triangle(n):
    if n <= 0:
        return []
    l = []
    for i in range(n):
        l.append([1] * (i + 1))
    return l
