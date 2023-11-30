#!/usr/bin/python3
def magic_calculation(a, b):
    if a > b:
        result = a + b
    else:
        result = 0
        for i in range(4, 6):
            result += i
    return result
