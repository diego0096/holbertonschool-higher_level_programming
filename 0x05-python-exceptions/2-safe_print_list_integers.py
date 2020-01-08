#!/bin/usr/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for num in range(x):
        try:
            print("{:d}".format(my_list[num]), end="")
            n += 1
        except(TypeError, ValueError, IndexError):
            pass
    print()
    return n
