#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        if i != j:
            print(f"{i}{j}", end="")
            if j == 9 and i + 1 == j:
                print(end="\n")
            else:
                print(end=", ")