#!/usr/bin/python3
for index1 in range(8):
    for index2 in range(index1 + 1, 10):
        print(f"{index1:d}{index2:d}", end=", ")
print(f"{index1 + 1:d}{index2:d}")
