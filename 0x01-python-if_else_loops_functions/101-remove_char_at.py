#!/usr/bin/python3
def remove_char_at(str, n):
    i = ""
    j = 0
    for h in str:
        if (j != n):
            i = i + h
        j = j + 1
    return(i)
