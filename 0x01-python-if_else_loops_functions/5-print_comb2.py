#!/usr/bin/python3
for n in range(0, 100):
    if n in range(0, 99):
        print("{}, ".format(format(n, '02d')), end = '')
    else:
        print(n)
