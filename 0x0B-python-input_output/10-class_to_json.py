#!/usr/bin/python3
def class_to_json(obj):
    """returns dictionary representation of JSON object"""
    return obj.__dict__
