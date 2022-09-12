#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new = []
    for i in range(0, 2):
        if i > len(tuple_a) - 1:
            a = 0
        else:
            a = tuple_a[i]
        if i > len(tuple_b) - 1:
            b = 0
        else:
            b = tuple_b[i]
        new.append(a + b)
    new = tuple(new)
    return new
