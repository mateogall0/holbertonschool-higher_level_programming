#!/usr/bin/python3
"""Module"""


import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Class to json_string"""
        if list_dictionaries is None:
            return []

        return json.dumps(list_dictionaries)
