#!/usr/bin/python3
def atoi(string):
    res = 0
    for i in range(len(string)):
        res = res * 10 + (ord(string[i]) - ord('0'))
    return res


if __name__ == '__main__':
    import sys
    argc = len(sys.argv)
    result = 0
    for i in range(1, argc):
        result += atoi(sys.argv[i])
    print("{}".format(result))
