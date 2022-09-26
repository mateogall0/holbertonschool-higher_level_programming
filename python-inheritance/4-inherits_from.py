#!/usr/bin/python3
"""Module"""


def inherits_from(obj, a_class):
    """Inherits from"""
    if type(obj) == a_class or not isinstance(obj, a_class):
        return False
    return True
