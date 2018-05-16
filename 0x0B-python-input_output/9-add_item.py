#!/usr/bin/python3
"""this script dds all arguments to a Python list and saves them in file"""
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
args = sys.argv[1:]
try:
    list_1 = load_from_json_file(filename)
    save_to_json_file(list_1 + args, filename)
except Exception:
    save_to_json_file(args, filename)
