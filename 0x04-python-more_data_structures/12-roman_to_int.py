#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) is str:
        num = 0
        holder = 0
        prev = 10000
        for c in roman_string:
            if c in dic:
                holder = dic[c]
            else:
                return (0)
            if holder <= prev:
                num += holder
                prev = holder
            else:
                num += holder - prev * 2
        return num
    return 0
