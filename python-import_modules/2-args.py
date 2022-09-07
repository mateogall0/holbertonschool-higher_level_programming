#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argc = len(sys.argv) - 1
    j = 1
    if argc == 0:
        print('0 arguments.')
        exit()
    print('{} arguments:'.format(argc))
    for i in sys.argv:
        print('{:n}: {:s}'.format(j, i))
        j += 1
