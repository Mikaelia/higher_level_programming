#!/usr/bin/python3
import os

def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
