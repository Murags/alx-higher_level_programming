#!/usr/bin/python3
def max_integer(my_list=[]):
    max1 = 0
    if my_list:
        for i in my_list:
            if i > max1:
                max1 = i
        return max1
    else:
        return None
