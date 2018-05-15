#!/usr/bin/python3
def is_same_class(obj, a_class):
    """Checks if object is exactly same as specified class
        Return: True if true, else False"""
    return a_class is type(obj)
