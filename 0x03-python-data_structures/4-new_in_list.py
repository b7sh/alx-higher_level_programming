#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list.copy()
    if idx < 0:
        return new
    ln = len(new)
    if idx > ln - 1:
        return new
    new[idx] = element
    return new
