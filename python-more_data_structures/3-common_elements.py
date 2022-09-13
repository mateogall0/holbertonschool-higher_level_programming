#!/usr/bin/python3
def common_elements(set_1, set_2):
    l1 = list(set_1)
    l2 = list(set_2)
    new = []

    for i in l1:
        for j in l2:
            if i == j:
                new.append(i)
    return dict.fromkeys(new)
