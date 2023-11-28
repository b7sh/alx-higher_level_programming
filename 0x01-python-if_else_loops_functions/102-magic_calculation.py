#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a > b and a <= 2:
        return a + b
    elif a < b:
        return c
    elif a > 2 and a > b:
        return (a * b) - c
