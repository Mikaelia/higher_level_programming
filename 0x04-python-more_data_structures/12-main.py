#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = ""
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "II"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "ID"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
