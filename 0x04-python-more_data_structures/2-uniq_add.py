#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    new = []
    for item in my_list:
        if item not in new:
            new.append(item)
            result += item
    return result
