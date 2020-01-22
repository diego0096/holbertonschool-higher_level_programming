#!/usr/bin/python3
import json
"""Function that writes an object using JSON representation"""


def save_to_json_file(my_obj, filename=""):
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
