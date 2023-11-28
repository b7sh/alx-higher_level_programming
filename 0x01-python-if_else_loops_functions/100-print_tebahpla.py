#!/usr/bin/python3
for s in range(122, 96, -1):
    if s % 2 == 0:
        s = chr(s).lower()
    else:
        s = chr(s).upper()
    print("{}".format(s), end="")
