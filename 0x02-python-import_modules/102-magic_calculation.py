#!/usr/bin/python
def magic_calculation(a, b):
    from magic_caculation import add, sub
    if a < b:
        c = add(a, b)
    for i in range(4, 6):
        c = add(c, b)
        return c
    return sub(a, b)
