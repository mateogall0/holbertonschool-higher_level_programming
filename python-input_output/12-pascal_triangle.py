#!/usr/bin/python3
"""Module"""


def pascal_triangle(n):
    """Pascal triangle"""
    if n <= 0:
        return []
    lis = []
    for i in range(n):
        lis.append([1] * (i + 1))
    try:
        for i in range(2, len(lis)):
            for j in range(1, len(lis[i]) - 1):
                lis[i][j] = lis[i - 1][j - 1] + lis[i - 1][j]
    except Exception:
        pass
    return lis
