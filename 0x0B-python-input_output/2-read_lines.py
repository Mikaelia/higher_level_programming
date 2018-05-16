#!/usr/bin/python3
import os

def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0 or nb_lines is False:
            for line in f:
                print(line, end='')
        for i, v in enumerate(f):
            if i < nb_lines:
                print(v, end='')
