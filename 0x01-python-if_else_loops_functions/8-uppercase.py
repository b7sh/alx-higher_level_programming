#!/usr/bin/python3
def uppercase(str):
    result = ""
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            result += chr(ord(s) - 32)
        else:
            result += s
    print(f"{result}")
