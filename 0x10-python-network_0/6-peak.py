#!/usr/bin/python3
def find_peak(list_of_integers):
    if not len(list_of_integers):
        return
    for i, v in enumerate(list_of_integers):
        if i > 1:
            if v < list_of_integers[i-1]:
                if list_of_integers[i-2] < list_of_integers[i-1]:
                        return list_of_integers[i-1]
    return max(list_of_integers)
