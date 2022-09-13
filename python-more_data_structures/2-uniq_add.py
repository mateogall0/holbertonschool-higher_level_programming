#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    res = 0
    for i in my_list:
        for j in new:
            if j == i:
                new.remove(i)
                break
        new.append(i)
    for i in new:
        res += i
    return res
