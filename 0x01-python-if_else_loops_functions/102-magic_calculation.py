#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a > b and a <= 3:
        return a + b
    elif a < b:
        return c
    elif a > 3 and a > b:
        return (a * b) - c
