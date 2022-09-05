#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
print(f"Last digit of {number} is {number % 10} ", end='')
if last < 6 and last != 0:
    print("and is less than 6 and not 0")
elif last == 0:
    print("and is 0")
else:
    print("and is grater than 5")
