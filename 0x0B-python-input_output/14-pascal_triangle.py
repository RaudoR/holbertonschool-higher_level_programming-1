#!/usr/bin/python3
def pascal_triangle(n):
    """creatign pascals triangle
    Args:
        n: input number of height of triangle
    Return:
        list of tirangle or empty list when n is lower and equal to 0
    """
    if n <= 0:
        return list()
    if n == 1:
        return [[1]]
    tri = [[1], [1, 1]]
    for i in range(2, n):
        tmp = [1]
        for j in range(1, i):
            tmp.append(tri[i - 1][j - 1] + tri[i - 1][j])
        tmp.append(1)
        tri.append(tmp)
    return tri
