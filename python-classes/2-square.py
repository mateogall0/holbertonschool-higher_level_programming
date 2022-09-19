#!/usr/bin/python3
"""Square"""


class Square():
    """Square"""
    __size = None

    def __init__(self, size=0):
        try:
            if size % 1 != 0:
                raise TypeError()
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")
