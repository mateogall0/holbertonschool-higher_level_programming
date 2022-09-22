#!/usr/bin/python3
"""text"""


def text_indentation(text):
    """text"""
    if type(text) != str:
        raise TypeError('text must be a string')
    t = text
    s = ''

    i = 0
    while i < len(t):
        s += t[i]
        if t[i] == ':' or t[i] == '?' or t[i] == '.':
            s += '\n\n'
            while i < len(t) and t[i] == ' ':
                i += 1
        i += 1
    print(s)
