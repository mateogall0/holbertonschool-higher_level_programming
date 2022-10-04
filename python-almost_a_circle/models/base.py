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
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save to file"""
        s = '[]'
        file_name = str(cls.__name__) + '.json'
        with open(file_name, 'w') as f:
            if list_objs:
                s = '['
                j = 0
                for i in list_objs:
                    s += i.to_json_string(i.to_dictionary())
                    if j != len(list_objs) - 1:
                        s += ', '
                    j += 1
                s += ']'
            f.write(s)
        return s

    @staticmethod
    def from_json_string(json_string):
        """From json string function"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create method"""
        if cls.__name__ == 'Square':
            o = cls(1)
        else:
            o = cls(1, 1)
        o.update(**dictionary)
        return o

    @classmethod
    def load_from_file(cls):
        """Load from file function"""
        a = []
        j = []
        file_name = cls.__name__ + '.json'
        try:
            with open(file_name, 'r') as f:
                j = cls.from_json_string(f.read())
            for i in j:
                a.append(cls.create(**i))
        except Exception:
            return []
        return a
