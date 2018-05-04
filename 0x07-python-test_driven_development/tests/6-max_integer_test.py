import unittest
"""Unittest for max_integer([..])
"""
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_findmax(self):
        self.assertEqual(max_integer([1,2,3]) , 3)
        self.assertEqual(max_integer([1,2,-3]) , 2)
        self.assertEqual(max_integer([]) , None)
        self.assertEqual(max_integer([1,2]) , 2)
        self.assertEqual(max_integer([-1,-22]) , -1)
