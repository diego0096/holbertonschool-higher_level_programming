#!/usr/bin/python3
def search_replace(my_list, search, replace):
    a = []
    for n in my_list:
        if n == search:
            a.append(replace)
        else:
            a.append(a)
    return a
