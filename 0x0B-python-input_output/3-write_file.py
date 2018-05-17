#!/usr/bin/python3
def write_file(filename="", text=""):
    """writes string to text file and returns number of characters"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
