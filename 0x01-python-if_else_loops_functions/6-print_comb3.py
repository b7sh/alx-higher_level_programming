#!/usr/bin/python3
for index1 in range(8):
    for index2 in range(index1 + 1, 10):
        print("{:d}{:d}".format(index1, index2), end=", ")
print("{:d}{:d}".format(index1 + 1, index2))
