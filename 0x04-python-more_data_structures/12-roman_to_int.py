#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string) is not None and type(roman_string) is str:
        mylist = []
        mydict = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}
        for i, v in enumerate(roman_string):
            if v in mydict:
                mylist.append(mydict.get(v))
                if v != "I" and roman_string[i - 1] is "I" and i > 0:
                    mylist.append(-2)
        return(sum(mylist))
    return(0)
