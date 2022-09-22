#!/usr/bin/python3
"""text"""


def text_indentation(text):
    """text"""
    if type(text) != str:
        raise TypeError('text must be a string')
    t = text
    i = 0
    while i < len(t):
        print(t[i], end='')
        if t[i] in ':?.' or t[i] == '\n':
            print(end='\n\n')
            i += 1
            while i < len(t) and (t[i] == ' ' or t[i] == '\t'):
                i += 1
            continue
        i += 1
