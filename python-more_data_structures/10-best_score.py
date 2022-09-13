#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max = None
    for key in sorted(a_dictionary.keys()):
        if not max or a_dictionary[max] < a_dictionary[key]:
            max = key
    return max
