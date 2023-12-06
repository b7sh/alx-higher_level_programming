#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    keys = list(a_dictionary.keys())
    keys.sort()
    a_dictionary[key] = value
    for item in keys:
        print("{}: {}".format(item, a_dictionary.get(item)))
