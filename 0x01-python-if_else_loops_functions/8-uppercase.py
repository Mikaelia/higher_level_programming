#!/usr/bin/python3
def uppercase(str):
    for c in str:
        c = ord(c)
        if (c <= 122 and c >= 97):
            c -= 32
        print("{:c}".format(c), end='')
    print('')
