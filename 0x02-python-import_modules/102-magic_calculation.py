#!/usr/bin/python3
def magic_calculation(a, b):
    from calculator_1 import add, sub
    if a > b:
        result = add(a, b)
    else:
        result = 0
        for i in range(4, 6):
            result = add(result, i)
        return result
    return sub(a, b)
