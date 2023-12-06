#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for item in range(len(my_list)):
        if my_list.count(item) < 1:
            continue
        else:
            result += item
    return result
