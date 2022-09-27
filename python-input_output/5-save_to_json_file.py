#!/usr/bin/python3
"""Module"""


import json


def save_to_json_file(my_obj, filename):
    """Save to json file"""
    with open(filename, 'w') as f:
        jobj = json.dumps(my_obj)
        f.write(jobj)
