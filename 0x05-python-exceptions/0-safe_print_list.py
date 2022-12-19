#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list:
        count = 0
        try:
            for i in range(0,x):
                if i == x - 1:
                    print("{}".format(my_list[i]))
                else:
                    print("{}".format(my_list[i]), end="")
                count += 1
            return count
        except:
            print()
            return count
