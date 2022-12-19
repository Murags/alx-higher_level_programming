#!/usr/bin/python3
from sys import stderr, exc_info
def safe_print_integer_err(value):
    file = stderr
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        print("Exception: {}".format(exc_info()[1]), file)
        return False
