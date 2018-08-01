#!/usr/bin/python3
"""find peak in a list of unsorted integers"""


def peak_finder(int_list, start, fin):
    """this usese recurrsion to find peak"""
    if start == fin:
        return int_list[start]
    mid = (fin + start) // 2
    if int_list[mid] < int_list[mid + 1]:
        return peak_finder(int_list, mid + 1, fin)
    return peak_finder(int_list, start, mid)


def find_peak(list_of_integers):
    """this function find the peak"""
    if not list_of_integers:
        return
    return peak_finder(list_of_integers, 0, len(list_of_integers) - 1)
