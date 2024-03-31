#!/usr/bin/python3
""" a function finds a peak in a list of unsorted integers. """
def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if list_of_integers == []:
        return None
    low = 0
    heigh = len(list_of_integers)
    mid = heigh // 2
    if heigh == 1:
        return list_of_integers[0]
    if heigh == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and \
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
