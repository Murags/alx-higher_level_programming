#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        result = 0
        j = 0
        for i in range(len(my_list)):
            j = 0
            while j < i:
                if my_list[j] == my_list[i]:
                    j += 1
                    break
                j += 1
            if my_list[j - 1] == my_list[i]:
               continue
            else:
                result += my_list[i];
        return result
