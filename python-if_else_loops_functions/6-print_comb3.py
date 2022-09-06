#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        if i != j and j == 9 and i + 1 == j:
            print("{:n}{:n}".format(i, j), end="\n")
        elif i != j:
            print("{:n}{:n}".format(i, j), end=", ")
