#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    ln = len(my_list)
    if idx > ln - 1:
        return my_list
    my_list[idx] = element
    return my_list
