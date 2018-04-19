#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    t_score = 0
    t_weight = 0
    for t in my_list:
        t_score += t[0] * t[1]
        t_weight += t[1]
    return t_score / t_weight
