#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argc = len(sys.argv)
    j = 1
    if argc == 1:
        print('0 arguments.')
        exit()
    print('{} arguments:'.format(argc))
    for i in range(1, argc):
        print('{:n}: {:s}'.format(j, sys.argv[i]))
        j += 1
