#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return
    a = []
    for n in a_dictionary:
        a.append(n)
    return max(a)
