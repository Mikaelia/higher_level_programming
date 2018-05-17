#!/usr/bin/python3
import os
import json


def load_from_json_file(filename):
    """creates an object from a JSON file"""
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
