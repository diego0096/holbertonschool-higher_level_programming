#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    b = [0, 0]
    for i, j in enumerate(tuple_a):
        if (i < 2):
            a[i] = tuple_a[i]
    for i, j in enumerate(tuple_b):
        if (i < 2):
            b[i] = tuple_b[i]
    sum1 = a[0] + b[0]
    sum2 = a[1] + b[1]
    return (sum1, sum2)
