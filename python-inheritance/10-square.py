#!/usr/bin/python3
"""Module"""


Rectangle = __import__('9-rectangle').Rectangle
"""Module"""


class Square(Rectangle):
    """Square"""
    def __init__(self, size):
        super().integer_validation("size", size)
        self.__size = size
        super().__init__(size, size)
