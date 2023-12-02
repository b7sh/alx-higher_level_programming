#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_1 = len(tuple_a)
    len_2 = len(tuple_b)

    if len_1 < 1:
        a1 = 0
        a2 = 0
    elif len_1 == 1:
        a1 = tuple_a[0]
        a2 = 0
    else:
        a1 = tuple_a[0]
        a2 = tuple_a[1]
    if len_2 < 1:
        b1 = 0
        b2 = 0
    elif len_2 == 1:
        b1 = tuple_b[0]
        b2 = 0
    else:
        b1 = tuple_b[0]
        b2 = tuple_b[1]

    new = (a1 + b1, a2 + b2)
    return new
