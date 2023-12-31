#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    roman = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    i = 0
    number = 0
    while i < len(roman_string):
        if (i + 1 < len(roman_string)) and \
                (roman[roman_string[i]] < roman[roman_string[i + 1]]):
            number += (roman[roman_string[i + 1]]-roman[roman_string[i]])
            i += 2
        else:
            number += roman[roman_string[i]]
            i += 1
    return number
