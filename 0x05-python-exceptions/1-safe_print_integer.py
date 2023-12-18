#!/usr/bin/python3
def safe_print_integer(value):
    is_int = False
    try:
        print("{:d}".format(value))
        is_int = True
        return is_int
    except ValueError:
        return is_int
