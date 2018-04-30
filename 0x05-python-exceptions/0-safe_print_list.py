#!/usr/bin/python3:
def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        for a in range(x):
            print(my_list[a], end="")
            num += 1
    except IndexError:
        print()
        return num
    else:
        print()
        return num
