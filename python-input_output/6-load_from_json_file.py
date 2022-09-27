#!/usr/bin/python3
"""Module"""


import json


def load_from_json_file(filename):
    """Load from json file"""
    with open(filename, 'r') as f:
        a = json.load(f)
        return a
