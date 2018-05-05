#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    test for max integer function
    """
    def test_docstring(self):
        doc = __import__('6-max_integer').__doc__
        self.assertIsNotNone(doc)
        self.assertIsNotNone(max_integer.__doc__)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_positive(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_one_item(self):
        self.assertEqual(max_integer([5]), 5)

    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, -1, -4, -5]), -1)

    def test_float(self):
        self.assertEqual(max_integer([2.5, 3.6, 2.9, 3.9]), 3.9)

    def test_character(self):
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

    def test_character(self):
        self.assertEqual(max_integer(["Hello", "World"]), "World")

    def test_string(self):
        self.assertRaises(TypeError, max_integer, [1, 2, "World"])
