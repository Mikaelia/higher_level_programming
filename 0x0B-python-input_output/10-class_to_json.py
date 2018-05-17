#!/usr/bin/python3
import os
import json


def class_to_json(obj):
    """returns dictionary representation of JSON object"""
    return obj.__dict__
