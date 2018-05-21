#!/usr/bin/python3
import unittest
import io
import sys
from models.rectangle import Rectangle
from models.base import Base

class TestRectangleClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.r1 = Rectangle(2, 3, 1, 1, 6)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_inheritance(self):
        self.assertIsInstance(self.r1, Base)
        self.assertIsInstance(self.r1, Rectangle)

    def test_initialization(self):
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.x, 1)
        self.assertEqual(self.r1.y, 1)
        self.assertEqual(self.r1.id, 6)

    def test_int_type(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle(1, {2}, 3, 4)
        with self.assertRaises(TypeError):
            r2 = Rectangle("f", 2, 3, 4)
        with self.assertRaises(TypeError):
            r2 = Rectangle(1, 2, "1", 4)
        with self.assertRaises(TypeError):
            r2 = Rectangle(1, 2, 3, {})

    def test_negative_or_zero(self):
        with self.assertRaises(ValueError):
            r2 = Rectangle(-1, 3)
        with self.assertRaises(ValueError):
            r2 = Rectangle(0, 3)
        with self.assertRaises(ValueError):
            r2 = Rectangle(11, -2)
        with self.assertRaises(ValueError):
            r2 = Rectangle(11, 0)

        # test x and y > 0
        with self.assertRaises(ValueError):
            r2 = Rectangle(1, 3, -1, 0)
        with self.assertRaises(ValueError):
            r2 = Rectangle(1, 3, 0, -2)
        # zero OK
        r2 = Rectangle(1, 3, 0, 0)

    def test_area(self):
        self.assertEqual(self.r1.area(), 6) # 2 * 3

    def test_str(self):
        output = self.r1.__str__()
        self.assertEqual(output, "[Rectangle] (6) 1/1 - 2/3")
        r2 = Rectangle(1, 3, 0, 0, 1)
        output = r2.__str__()
        self.assertEqual(output, "[Rectangle] (1) 0/0 - 1/3")

    def test_display_output(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.r1.display()
        sys.stout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "\n ##\n ##\n ##\n")

    def test_update_method(self):
        r6 = Rectangle(1, 1, 1, 1, 1)
        r6.update(2, 2, 2, 2, 2)
        output = r6.__str__()
        self.assertEqual(output, "[Rectangle] (2) 2/2 - 2/2")
        r6.update(3, 4)
        output = r6.__str__()
        self.assertEqual(output, "[Rectangle] (3) 2/2 - 4/2")

    def test_update_method_args_kwargs(self):
        r7 = Rectangle(1, 1)
        r7.update(7)
        r7.update(width=1, x=2)
        output = r7.__str__()
        self.assertEqual(output, '[Rectangle] (7) 2/0 - 1/1')
        r7.update(x=1, height=2, y=3, width=4, id=99)
        output = r7.__str__()
        self.assertEqual(output, '[Rectangle] (99) 1/3 - 4/2')

    def test_to_dict(self):
        r8 = Rectangle(1, 2, 3, 4, 5)
        mydict = r8.to_dictionary()
        self.assertEqual(mydict['id'], 5)
        self.assertEqual(mydict['height'], 2)
        self.assertEqual(mydict['width'], 1)
        self.assertEqual(mydict['x'], 3)
        self.assertEqual(mydict['y'], 4)
