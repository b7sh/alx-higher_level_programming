#!/usr/bin/python
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError as e):
        print("Exception: {}".forma(e), file=sys.stderr)
        return False
