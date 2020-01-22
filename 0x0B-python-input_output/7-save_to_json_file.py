#!/usr/bin/python3
import json
"""Function that writes an object using JSON representation"""


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
