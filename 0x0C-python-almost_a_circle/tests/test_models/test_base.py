#!/usr/bin/python3
"""unitest for base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """testing for base class"""
    def test_docstring(self):
        """test if it has docstring"""
        self.assertIsNotNone(Base.__doc__)

    def test_init(self):
        """test if init works with no args"""
        t1 = Base()
        self.assertEqual(t1.id, 1)
        t2 = Base()
        self.assertEqual(t2.id, 2)

    def test_passing_args(self):
        """test passing in args and empty"""
        t1 = Base(15)
        self.assertEqual(t1.id, 15)
        t2 = Base(20)
        self.assertEqual(t2.id, 20)
        t3 = Base()
        self.assertEqual(t3.id, 3)
        t4 = Base(-5)
        self.assertEqual(t4.id, -5)
