#!/usr/bin/python3
import unittest
import io
import sys
from models.square import Square
from models.base import Base

class TestSquareClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s1 = Square(2, 1, 1)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_inheritance(self):
        self.assertIsInstance(self.s1, Base)
        self.assertIsInstance(self.s1, Square)

    def test_initialization(self):
        self.assertEqual(self.s1.size, 2)
        self.assertEqual(self.s1.x, 1)
        self.assertEqual(self.s1.y, 1)
        self.assertEqual(self.s1.id, 1)

    def test_int_type(self):
        with self.assertRaises(TypeError):
            s2 = Square(1, {2}, 3)
        with self.assertRaises(TypeError):
            s2 = Square("f", 2)
        with self.assertRaises(TypeError):
            s2 = Square(1, 2, "1")
        with self.assertRaises(TypeError):
            s2 = Square("3", 2, 3)

    def test_negative_or_zero(self):
        with self.assertRaises(ValueError):
            s2 = Square(-1, 3)
        with self.assertRaises(ValueError):
            s2 = Square(0, 3)
        with self.assertRaises(ValueError):
            s2 = Square(11, -2)
        with self.assertRaises(ValueError):
            s2 = Square(11, -1000000, 0)

        # x, y zero OK
        s2 = Square(1, 0)

    def test_area(self):
        self.assertEqual(self.s1.area(), 4)

    def test_str(self):
        output = self.s1.__str__()
        self.assertEqual(output, "[Square] (1) 1/1 - 2")
        s2 = Square(1, 3, 0)
        output = s2.__str__()
        self.assertEqual(output, "[Square] (3) 3/0 - 1")

    def test_display_output(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.s1.display()
        sys.stout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "\n ##\n ##\n")

    def test_update_method(self):
        s6 = Square(1, 1, 1)
        s6.update(2, 2, 2)
        output = s6.__str__()
        self.assertEqual(output, "[Square] (2) 2/1 - 2")
        s6.update(3, 4)
        output = s6.__str__()
        self.assertEqual(output, "[Square] (3) 2/1 - 4")

    def test_update_kwargs(self):
        s7 = Square(1, 1)
        s7.update(7)
        s7.update(size=2, x=2, y=3)
        output = s7.__str__()
        self.assertEqual(output, '[Square] (7) 2/3 - 2')
        s7.update(x=1, y=3, id=99)
        output = s7.__str__()
        self.assertEqual(output, '[Square] (99) 1/3 - 2')

    def test_to_dict(self):
        s8 = Square(1, 2, 3, 4)
        mydict = s8.to_dictionary()
        self.assertEqual(mydict['id'], 4)
        self.assertEqual(mydict['size'], 1)
        self.assertEqual(mydict['x'], 2)
        self.assertEqual(mydict['y'], 3)
