#!/usr/bin/python3
"""reads a text file and prints to stdout"""
import os


def read_file(filename=""):
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
