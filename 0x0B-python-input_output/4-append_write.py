#!/usr/bin/python3
"""appends string to text file and returns characters added"""
import os


def append_write(filename="", text=""):
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
