#!/usr/bin/python3
def max_integer(my_list=[]):
    ln = len(my_list)
    if ln == 0:
        return None
    else:
        max_num = 1
        for item in my_list:
            if item > max_num:
                max_num = item
        return max_num
