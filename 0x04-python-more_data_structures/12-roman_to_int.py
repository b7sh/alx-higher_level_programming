#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    i = 0
    number = 0
    while i < len(roman_string):
        if(i + 1 < len(roman_stirng):
            if(roman[roman_string[i]] < roman[roman_string[i + 1]]:
                num+=(roman[roman_string[i + 1]]-roman[roman_string[i]])
                i+=2
        else:
        num += roman[roman_string[i]]
        i+=1
    if roman_string == None:
        return 0
    return num
