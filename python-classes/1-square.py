#!/usr/bin/python3
"""Square"""


class Square():
    """Square"""
    __size = None

    def __init__(self, new_size=None):
        if new_size:
            self.__size = new_size
