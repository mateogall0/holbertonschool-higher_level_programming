#!/usr/bin/python3
"""Module"""


import json


def from_json_string(my_str):
    """To json string"""
    jstr = json.loads(my_str)
    return(jstr)
