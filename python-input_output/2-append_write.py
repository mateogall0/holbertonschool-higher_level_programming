#!/usr/bin/python3
"""Module"""


def append_write(filename="", text=""):
    """Write file"""
    with open(filename, 'a') as f:
        return f.write(text)
