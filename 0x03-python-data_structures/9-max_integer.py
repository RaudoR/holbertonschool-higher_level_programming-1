#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        num = 0
        for i in my_list:
            if i > num:
                num = i
        return num
    return
