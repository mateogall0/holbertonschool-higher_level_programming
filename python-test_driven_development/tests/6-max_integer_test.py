#!/usr/bin/python3
"""unittest"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestStringMethods(unittest.TestCase):
    """TestStringMethods"""
    def test_0(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
    def test_1(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)
    def test_2(self):
        self.assertEqual(max_integer([4, 2, 3]), 4)
    def test_3(self):
        self.assertEqual(max_integer([4, -2, 3]), 4)
    def test_3(self):
        self.assertEqual(max_integer([-4, -2, -3]), -2)
    def test_4(self):
        self.assertEqual(max_integer([4]), 4)
    def test_5(self):
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
