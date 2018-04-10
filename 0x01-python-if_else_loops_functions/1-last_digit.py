#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_num = 1
n = 0
if number < 0:
    l_num = -1
    n = number * -1
l_num = n % 10 * l_num
if l_num > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, l_num))
elif l_num == 0:
    print("Last digit of {} is {} and is 0".format(number, l_num))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, l_num))
