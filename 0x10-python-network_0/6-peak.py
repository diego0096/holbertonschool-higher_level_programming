#!/usr/bin/python3
def find_peak(list_of_integers):
    """ Python function to find peak number"""
    l = len(list_of_integers)
    if l == 0:
        return
    k = l // 2
    pivot = list_of_integers[k]
    left = list_of_integers[k - 1]

    if (k == l - 1 or pivot >= list_of_integers[k + 1]) and\
            (k == 0 or pivot >= left):
        return pivot
    elif k != l - 1 and list_of_integers[m + 1] > pivot:
        return (find_peak(list_of_integers[k + 1:]))
    return (find_peak(list_of_integers[:k]))
