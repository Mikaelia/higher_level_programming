#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    #ID tests:
    @classmethod
    def setUpClass(cls):
        cls.b = Base()
        cls.b1 = Base(None)
        cls.b2 = Base()
        cls.b3 = Base()
        cls.b4 = Base(7)
        cls.b5 = Base()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_is_instance(self):
        self.assertIsInstance(self.b, Base)

    def test_no_id(self):
        self.assertEqual(self.b1.id, 2)
        self.assertEqual(self.b2.id, 3)
        self.assertEqual(self.b3.id, 4)

    def test_given_id(self):
        self.assertEqual(self.b4.id, 7)
        self.assertEqual(self.b5.id, 5)

if __name__ == '__main__':
    unittest.main()
