#!/usr/bin/python3
def magic_calculation(a, b):
    #from magic_calculation import add, sub
    if a < b:
        result = a + b
    elif a > b:
        result = 0
        for i in range(4, 6):
            result += i
    return result
