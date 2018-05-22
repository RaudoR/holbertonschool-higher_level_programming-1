#!/usr/bin/python3
"""unitest for Square"""
import unittest
import io
import sys
from models.square import Square


class TestSquare(unittest.TestCase):
    """testing for Square class"""
    def test_docstring(self):
        """test if it has docstring"""
        self.assertIsNotNone(Square.__doc__)

    def test_init(self):
        """test if init works"""
        t1 = Square(8, 10, 10, 15)
        self.assertEqual(t1.width, 8)
        self.assertEqual(t1.height, 8)
        self.assertEqual(t1.x, 10)
        self.assertEqual(t1.y, 10)
        self.assertEqual(t1.id, 15)

    def test_init2(self):
        """test if init works with just height and width"""
        t1 = Square(10)
        self.assertEqual(t1.width, 10)
        self.assertEqual(t1.height, 10)
        self.assertEqual(t1.x, 0)
        self.assertEqual(t1.y, 0)

    def test_not_int(self):
        """test if not int"""
        with self.assertRaises(TypeError):
            Square("Yo")

    def test_negative(self):
        """test if negative"""
        with self.assertRaises(ValueError):
            Square(-50)

    def test_zero(self):
        """test if zero"""
        with self.assertRaises(ValueError):
            Square(0)

    def test_x_int(self):
        """test if x is not int"""
        with self.assertRaises(TypeError):
            Square(2, "Yo")

    def test_x_int(self):
        """test if x is negative"""
        with self.assertRaises(ValueError):
            Square(2, -5)

    def test_y_int(self):
        """test if y is not int"""
        with self.assertRaises(TypeError):
            Square(2, 5, "Yo")

    def test_y_int(self):
        """test if y is negative"""
        with self.assertRaises(ValueError):
            Square(2, 5, -5)

    def test_area(self):
        """test if area works with just 2 arguments"""
        t1 = Square(10)
        self.assertEqual(t1.area(), 100)

    def test_area2(self):
        """test if area works with all arguments"""
        t1 = Square(5, 3, 5, 15)
        self.assertEqual(t1.area(), 25)

    def test_display(self):
        """check display square with #"""
        holder = io.StringIO()
        sys.stdout = holder
        t1 = Square(2)
        t1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(holder.getvalue(), "##\n##\n")

    def test_str_return(self):
        """check if the str returns right"""
        t1 = Square(4, 2, 1, 12)
        self.assertEqual(t1.__str__(), "[Square] (12) 2/1 - 4")

    def test_display_with_xy(self):
        """check if display with cordinates work"""
        holder = io.StringIO()
        sys.stdout = holder
        t1 = Square(2, 2, 2, 10)
        t1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(holder.getvalue(), "\n\n  ##\n  ##\n")

    def test_size_setter(self):
        """check if size setts work"""
        t1 = Square(4, 2, 1, 12)
        t1.size = 20
        self.assertEqual(t1.__str__(), "[Square] (12) 2/1 - 20")

    def test_size_fail(self):
        """test if size setter fail"""
        t1 = Square(4, 2, 1, 12)
        with self.assertRaises(TypeError):
            t1.size = "yo"
        with self.assertRaises(ValueError):
            t1.size = -20

    def test_update(self):
        """check if update works right"""
        t1 = Square(10, 10, 10, 10)
        t1.update(89)
        self.assertEqual(t1.__str__(), "[Square] (89) 10/10 - 10")
        t1.update(89, 2)
        self.assertEqual(t1.__str__(), "[Square] (89) 10/10 - 2")
        t1.update(89, 2, 3)
        self.assertEqual(t1.__str__(), "[Square] (89) 3/10 - 2")
        t1.update(89, 2, 3, 4)
        self.assertEqual(t1.__str__(), "[Square] (89) 3/4 - 2")

    def test_update_size_check(self):
        """check if update checks size validation"""
        t1 = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            t1.update(89, "Yo", 3, 4)
        with self.assertRaises(ValueError):
            t1.update(89, -5, 3, 4)
        with self.assertRaises(ValueError):
            t1.update(89, 0, 3, 4)

    def test_update_x_check(self):
        """check if update checks x validation"""
        t1 = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            t1.update(89, 3, "Yo", 5)
        with self.assertRaises(ValueError):
            t1.update(89, 5, -4, 5)

    def test_update_y_check(self):
        """check if update checks y validation"""
        t1 = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            t1.update(89, 3, 4, "yo")
        with self.assertRaises(ValueError):
            t1.update(89, 5, 4, -5)

    def test_update_kwargs_check(self):
        """check if kwars update works"""
        t1 = Square(10, 10, 10, 10)
        t1.update(size=1)
        self.assertEqual(t1.__str__(), "[Square] (10) 10/10 - 1")
        t1.update(size=2, x=2)
        self.assertEqual(t1.__str__(), "[Square] (10) 2/10 - 2")
        t1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(t1.__str__(), "[Square] (89) 3/1 - 2")

    def test_update_kwargs_with_args(self):
        """check if args exist it ignores kwargs"""
        t1 = Square(10, 10, 10, 10)
        t1.update(24, 3, x=1)
        self.assertEqual(t1.__str__(), "[Square] (24) 10/10 - 3")

    def test_dictionary_check(self):
        dic = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        t1 = Square(10, 2, 1, 1)
        self.assertEqual(dic, t1.to_dictionary())
