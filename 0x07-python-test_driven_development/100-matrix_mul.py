#!/usr/bin/python3
"""
This module multiply 2 matricies
"""


def matrix_mul(m_a, m_b):
    """
    multiply 2 matrix that is given
    Args:
        m_a: input first matrix
        m_b: input second matrix
    Raises:
        TypeError: if m_a or m_b is not list
        ValueError: if m_a or m_b is None
        TypeError: if both matricies don't have an int or float
        TypeError: if both matricies are not rectagles or squares
    Returns:
        return m_a * m_b
    """
    if type(m_a) is not list or\
       not all(isinstance(l_a, list) for l_a in m_a):
        raise TypeError("m_a must be a list")
    if type(m_b) is not list or\
       not all(isinstance(l_b, list) for l_b in m_b):
        raise TypeError("m_b must be a list")
    if m_a == [] or not all(l_a != [] for l_a in m_a):
        raise ValueError("m_a can't be empty")
    if m_b == [] or not all(l_b != [] for l_b in m_b):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(i_a, (int, float)) for l_a in m_a for i_a in l_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(i_b, (int, float)) for l_b in m_b for i_b in l_b):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(l_a) is len(m_a[0]) for l_a in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(l_b) is len(m_b[0]) for l_b in m_b):
        raise TypeError("each row of m_b must should be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    m_r = [[sum(a * b for a, b in zip(x, y))
            for y in zip(*m_b)]
           for x in m_a]
    return m_r
