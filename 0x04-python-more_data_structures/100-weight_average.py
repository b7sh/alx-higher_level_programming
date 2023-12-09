#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    x = 0
    y = 0
    for n in my_list:
        x += (n[0] * n[1])
        y += n[1]
    z = x / y
    return z
