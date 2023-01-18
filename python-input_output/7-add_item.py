#!/usr/bin/python3
"""JSON"""


import json
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

arg = sys.argv[1:]
file_name = "add_item.json"

try:
    python_object = load_from_json_file(file_name)
except FileNotFoundError:
    save_to_json_file([], file_name)

python_object = load_from_json_file(file_name)
if type(python_object) is list:
    for item in arg:
        python_object.append(item)

save_to_json_file(python_object, file_name)
