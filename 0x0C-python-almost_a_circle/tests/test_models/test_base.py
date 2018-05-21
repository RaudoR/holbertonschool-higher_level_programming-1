#!/usr/bin/python3
"""unitest for base"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """testing for base class"""

    def test_docstring(self):
        """test if it has docstring"""
        self.assertIsNotNone(Base.__doc__)

    def test_a_init(self):
        """test if init works with no args"""
        t1 = Base()
        self.assertEqual(t1.id, 1)
        t2 = Base()
        self.assertEqual(t2.id, 2)

    def test_a_passing_args(self):
        """test passing in args and empty"""
        t1 = Base(15)
        self.assertEqual(t1.id, 15)
        t2 = Base(20)
        self.assertEqual(t2.id, 20)
        t3 = Base()
        self.assertEqual(t3.id, 3)
        t4 = Base(-5)
        self.assertEqual(t4.id, -5)


    def test_json_dictionary(self):
        """test if disctionary does return"""
        t1 = Rectangle(10, 7, 2, 8, 1)
        dic = t1.to_dictionary()
        new_json_dic = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_dic = Base.to_json_string([dic])
        self.assertEqual(dic, new_json_dic)
        self.assertEqual(type(dic), dict)
        self.assertEqual(type(json_dic), str)

    def test_json_dictionary_empty(self):
        """test if disctionary is empty"""
        dic = Base.to_json_string([])
        self.assertEqual(dic, "[]")

    def test_json_file_created(self):
        """test if file is created with Json string"""
        t1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([t1])
        with open("Rectangle.json", "r") as f:
            self.assertEqual([t1.to_dictionary()], json.load(f))

    def test_json_file_empty(self):
        """test if file is created with empty"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual([], json.load(f))

    def test_json_file_empty(self):
        """test if file is created with still empty"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual([], json.load(f))

    def test_from_json_string(self):
        """test if json string converts back"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(json_list_input), str)
        self.assertEqual(type(list_output), list)
        self.assertEqual(list_output, list_input)

    def test_create_rectangle(self):
        """test making rectangle"""
        t1 = Rectangle(3, 5, 1)
        t1_dictionary = t1.to_dictionary()
        t2 = Rectangle.create(**t1_dictionary)
        self.assertNotEqual(t1, t2)

    def test_create_square(self):
        """test creating square"""
        t1 = Square(3, 5, 1)
        t1_dictionary = t1.to_dictionary()
        t2 = Rectangle.create(**t1_dictionary)
        self.assertNotEqual(t1, t2)

    def test_load_from_file_rectangle(self):
        """check if file load rectangle"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertNotEqual(list_rectangles_input, list_rectangles_output)

    def test_load_from_file_square(self):
        """check if file load square"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertNotEqual(list_squares_input, list_squares_output)

    def test_save_load_from_csv_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertTrue(list_rectangles_output[0].__str__()
                        == list_rectangles_input[0].__str__())
        self.assertTrue(list_rectangles_output[1].__str__()
                        == list_rectangles_input[1].__str__())
