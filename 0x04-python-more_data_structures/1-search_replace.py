#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    new = my_list.copy()
    for item in range(len(my_list)):
        if new[item] == search:
            new[item] = replace
    return new
