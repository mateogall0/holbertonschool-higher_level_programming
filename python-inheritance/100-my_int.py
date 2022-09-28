#!/usr/bin/python3
"""Module"""


class Int:
    """Class INT"""
    pass


class MyInt(Int):
    """MyINT"""
    def __init__(self, num):
        self.__num = num

    def __str__(self):
        return f'{self.__num}'

    def __eq__(self, other):
        if self.__num == other:
            return False
        return True

    def __ne__(self, other):
        if self.__num != other:
            return False
        return True
