#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    str_cpy = ""
    str_cpy = str[:n]
    str_cpy += str[n + 1:]
    return (str_cpy)
