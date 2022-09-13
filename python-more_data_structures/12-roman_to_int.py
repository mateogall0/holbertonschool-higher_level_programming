#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return None
    result = 0
    for i in roman_string:
        if i == 'I':
            result += 1
        if i == 'V':
            result += 5
        if i == 'X':
            result += 10
        if i == 'L':
            result += 50
        if i == 'C':
            result += 100
        if i == 'D':
            result += 500
        if i == 'M':
            result += 1000
    return result
