#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return
    num = 0
    for i in range(length):
        if my_list[i] > num:
            num = my_list[i]
    return num
