#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Convert the list to a set of unique integers
    unique_ints = set(my_list)
    # Convert the set back to a list and return the sum of the unique integers
    return sum(list(unique_ints))

