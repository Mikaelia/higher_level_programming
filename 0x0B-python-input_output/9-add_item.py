#!/usr/bin/python3
"""adds all arguments to a list and saves to file"""
import sys


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

args = []
for i, v in enumerate(sys.argv):
    if i > 0:
        args.append(v)
try:
    flist = load_from_json_file('add_item.json')
    save_to_json_file(flist + args, 'add_item.json')
except BaseException:
    save_to_json_file(args, 'add_item.json')
