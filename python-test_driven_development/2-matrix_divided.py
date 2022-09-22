#!/usr/bin/python3
"""matrix"""


def matrix_divided(matrix, div):
    """matrix resurrections"""
    if div == 0:
        raise ZeroDivisionError('division by zero')
    l = len(matrix[0])
    m = []
    for i in range(len(matrix)):
        if l != len(matrix[i]):
            raise TypeError('Each row of the matrix must have the same size')
        m.append([])
        for j in matrix[i]:
            if not isinstance(j, float) and not isinstance(j, int):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            m[i].append(round(j / div, 2))
    return m
