#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    '''Function that reads the lines of a text file and print it'''

    count = 0
    with open(filename, encoding="utf8") as f:
        for line in f:
            count += 1
            print(line, end="")
            if nb_lines == count:
                break
