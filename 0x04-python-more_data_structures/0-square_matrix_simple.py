#!/usr/bin/python3
def squared(x):
    return x**2


def square_matrix_simple(matrix=[]):
    new_m = []
    for l in matrix:
        new_m += [list(map(squared, l))]
    return new_m
