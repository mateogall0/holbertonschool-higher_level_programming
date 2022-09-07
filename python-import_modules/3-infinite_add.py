#!/usr/bin/python3
def atoi(string):
    res = 0
    sign = 1
    i = 0

    if string[0] == '-':
        sign = -1
        i += 1

    for j in range(i, len(string)):
        res = res * 10 + (ord(string[j]) - ord('0'))
    return res * sign


if __name__ == '__main__':
    import sys
    argc = len(sys.argv)
    result = 0
    for i in range(1, argc):
        result += atoi(sys.argv[i])
    print("{}".format(result))
