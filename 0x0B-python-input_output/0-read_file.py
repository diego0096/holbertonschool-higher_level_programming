#!/usr/bin/python3
def read_file(filename=""):
    '''read the content of the file'''

    with open(filename, encoding="utf8") as f:
        print(f.read(), end="")
