#!/usr/bin/python3
def no_c(my_string):
    new = list(my_string)
    for i in range(len(new)):
        if new[i] == 'c':
            new[i] == ''
