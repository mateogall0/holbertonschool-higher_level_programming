#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    exe = dir(hidden_4)
    exe.sort()
    for i in exe:
        if i[:2] != '__':
            print("{:s}".format(i))
