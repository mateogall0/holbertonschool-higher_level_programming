#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    for i in my_list:
        new.append(not i % 2)
    return new