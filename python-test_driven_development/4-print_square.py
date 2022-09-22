#!/usr/bin/python3
"""Square"""


def print_square(size):
    """Square"""
    if type(size) == float and size < 0:
        raise TypeError('size must be an integer')
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for _ in range(size):
        for _ in range(size):
            print('#', end='')
        print()
