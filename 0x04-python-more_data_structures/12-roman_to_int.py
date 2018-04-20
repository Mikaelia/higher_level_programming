#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string) and isinstance(roman_string, str) and str != "":
        mylist = []
        mydict = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}
        for i, v in enumerate(roman_string):
            if v in mydict:
                if i < (len(roman_string) -
                        1) and mydict.get(roman_string[i + 1]) > mydict.get(v):
                    mylist.append(-mydict.get(v))
                else:
                    mylist.append(mydict.get(v))
        return(sum(mylist))
    return(0)
