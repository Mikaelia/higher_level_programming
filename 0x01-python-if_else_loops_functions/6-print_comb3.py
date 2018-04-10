#!/usr/bin/python3
for i in range(1, 99):
    ones = i % 10
    tens = i / 10
    if (ones > tens):
        if (i != 89):
            print("{:02d}".format(i), end=", ")
        else:
            print("{:d}".format(i))
