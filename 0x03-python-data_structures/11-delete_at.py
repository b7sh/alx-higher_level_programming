#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    ln = len(my_list)
    if idx > ln - 1:
        return my_list
    else:
        my_list.remove(idx + 1)
    return my_list
