#!/usr/bin/pyton3
def number_of_lines(filename=""):
    '''return the number of lines of a text file'''

    count = 0
    with open(filename, encoding="utf8") as f:
        for line in f:
            count += 1
    return count
