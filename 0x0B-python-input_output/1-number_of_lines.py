#!/usr/bin/python3
"""returns number of lines in a text file"""
import os


def number_of_lines(filename=""):
    with open(filename, encoding='utf-8') as f:
        line_num = 0
        for line in f:
            line_num += 1
        return line_num
