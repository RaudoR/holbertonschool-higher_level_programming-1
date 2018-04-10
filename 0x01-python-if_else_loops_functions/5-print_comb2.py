#!/usr/bin/python3
for n in range(0,100):
    if n < 10:
        print(format(n, '02d'), end = '')
    else:
        print(n, end = '')
    if n in range(0, 99):
        print(", ", end = '')
    else:
        print()
