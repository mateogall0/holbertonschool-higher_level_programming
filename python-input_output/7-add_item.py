#!/usr/bin/python3
"""Module"""


import sys


import json


sfile = __import__('5-save_to_json_file').save_to_json_file


lfile = __import__('6-load_from_json_file').load_from_json_file


if __name__ == '__main__':
    a = []
    try:
        a = lfile('add_item.json')
    except Exception:
        pass
    for i in range(1, len(sys.argv)):
        a.append(sys.argv[i])
    sfile(a, 'add_item.json')
