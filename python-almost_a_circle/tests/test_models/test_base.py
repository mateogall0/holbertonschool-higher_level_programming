#!/usr/bin/python3
"""Module"""


import unittest
from models.base import Base


class testsNumber0(unittest.TestCase):
    """Test of Base() for assigning
    automatically an ID exists"""
    def setUp(self):
        self.base1 = Base()

    def test_0(self):
        self.assertEqual(self.base1.id, 1)


class testsNumber1(unittest.TestCase):
    """Tests number 1"""
    def setUp(self):
        self.base1 = Base(56)
    def test_1(self):
        self.assertEqual(self.base1.id, 56)

if __name__ == '__main__':
    unittest.main()
