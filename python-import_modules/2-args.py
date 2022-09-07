#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argc = len(sys.argv)
    j = 1
    if argc == 1:
        print('0 arguments.')
        exit()
    if argc - 1 == 1:
        print('1 argument:')
    else:
        print('{} arguments:'.format(argc - 1))
    for i in range(1, argc):
        print('{:n}: {:s}'.format(j, sys.argv[i]))
        j += 1
