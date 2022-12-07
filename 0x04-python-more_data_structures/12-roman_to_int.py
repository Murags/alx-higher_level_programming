#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str:
        result = 0
        for i in roman_string:
            if i == 'I':
                result += 1
            elif i == 'V':
                result += 5
            elif i == 'X':
                result += 10
            elif i == 'L':
                result += 50
            elif i == 'C':
                result += 100
            elif i == 'D':
                result += 500
            elif i == 'M':
                result += 1000
        return result
    else:
        return 0
