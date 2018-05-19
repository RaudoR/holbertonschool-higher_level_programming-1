#!/usr/bin/python3
"""unitest for Rectangle"""
import unittest
import io
import sys
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """testing for rectangle class"""
    def test_docstring(self):
        """test if it has docstring"""
        self.assertIsNotNone(Rectangle.__doc__)

    def test_init(self):
        """test if init works"""
        t1 = Rectangle(8, 9, 10, 10, 15)
        self.assertEqual(t1.width, 8)
        self.assertEqual(t1.height, 9)
        self.assertEqual(t1.x, 10)
        self.assertEqual(t1.y, 10)
        self.assertEqual(t1.id, 15)

    def test_init2(self):
        """test if init works with just height and width"""
        t1 = Rectangle(10, 2)
        self.assertEqual(t1.width, 10)
        self.assertEqual(t1.height, 2)
        self.assertEqual(t1.x, 0)
        self.assertEqual(t1.y, 0)

    def test_width_not_int(self):
        """test if width is not int"""
        with self.assertRaises(TypeError):
            Rectangle("Yo", 1)

    def test_width_negative(self):
        """test if width is negative"""
        with self.assertRaises(ValueError):
            Rectangle(-50, 2)

    def test_width_zero(self):
        """test if width is zero"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_int(self):
        """test if height is not int"""
        with self.assertRaises(TypeError):
            Rectangle(2, "Yo")

    def test_height_int(self):
        """test if height is negative"""
        with self.assertRaises(ValueError):
            Rectangle(2, -50)

    def test_height_zero(self):
        """test if height is zero"""
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_x_int(self):
        """test if x is not int"""
        with self.assertRaises(TypeError):
            Rectangle(2, 3, "Yo", 4)

    def test_x_int(self):
        """test if x is negative"""
        with self.assertRaises(ValueError):
            Rectangle(2, 3, -5, 4)

    def test_y_int(self):
        """test if y is not int"""
        with self.assertRaises(TypeError):
            Rectangle(2, 3, 5, "Yo")

    def test_y_int(self):
        """test if y is negative"""
        with self.assertRaises(ValueError):
            Rectangle(2, 3, 5, -5)

    def test_area(self):
        """test if area works with just 2 arguments"""
        t1 = Rectangle(10, 2)
        self.assertEqual(t1.area(), 20)

    def test_area2(self):
        """test if area works with all arguments"""
        t1 = Rectangle(8, 5, 3, 5, 15)
        self.assertEqual(t1.area(), 40)

    def test_display(self):
        """check display square with #"""
        holder = io.StringIO()
        sys.stdout = holder
        r1 = Rectangle(2, 2)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(holder.getvalue(), "##\n##\n")

    def test_str_return(self):
        """check if the str returns right"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_with_xy(self):
        """check if display with cordinates work"""
        holder = io.StringIO()
        sys.stdout = holder
        r1 = Rectangle(2, 2, 2, 2, 10)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(holder.getvalue(), "\n\n  ##\n  ##\n")

    def test_update(self):
        """check if update works right"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_update2(self):
        """check if update works with morearguments"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_width_check(self):
        """check if update checks width validation"""
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r1.update(89, "Yo", 3, 4, 5)
        with self.assertRaises(ValueError):
            r1.update(89, -5, 3, 4, 5)
        with self.assertRaises(ValueError):
            r1.update(89, 0, 3, 4, 5)

    def test_update_height_check(self):
        """check if update checks height validation"""
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r1.update(89, 3, "Yo", 4, 5)
        with self.assertRaises(ValueError):
            r1.update(89, 5, -3, 4, 5)
        with self.assertRaises(ValueError):
            r1.update(89, 3, 0, 4, 5)

    def test_update_x_check(self):
        """check if update checks x validation"""
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r1.update(89, 3, 5, "Yo", 5)
        with self.assertRaises(ValueError):
            r1.update(89, 5, 5, -4, 5)

    def test_update_y_check(self):
        """check if update checks y validation"""
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r1.update(89, 3, 4, 4, "yo")
        with self.assertRaises(ValueError):
            r1.update(89, 5, 3, 4, -5)
