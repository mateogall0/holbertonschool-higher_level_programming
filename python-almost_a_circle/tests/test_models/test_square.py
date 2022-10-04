#!/usr/bin/python3
"""Module"""


import unittest
from models.square import Square

class AllTests(unittest.TestCase):
    def test_0(self):
        self.s1 = Square(75, 62)
        self.s1.update()
        self.assertEqual(self.s1.id, 22)
        self.s1.update(89)
        self.assertEqual(self.s1.id, 89)
        self.s1.update(89, 1)
        self.assertEqual(self.s1.id, 89)
        self.assertEqual(self.s1.size, 1)
    def test_1(self):
        self.s2 = Square(1)
        self.assertEqual(self.s2.id, 23)
        self.assertEqual(self.s2.size, 1)
        self.s3 = Square(1, 2, 3)
        self.assertEqual(self.s3.id, 24)


if __name__ == '__main__':
    unittest.main()
