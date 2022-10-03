#!/usr/bin/python3
"""Module"""


import unittest
from models.rectangle import Rectangle


class testsNumber0(unittest.TestCase):
    """Test of Base() for assigning
    automatically an ID exists"""
    def test_0(self):
        self.r1 = Rectangle(1, 2)
        self.assertEqual(self.r1.id, 13)
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.height, 2)

if __name__ == '__main__':
    unittest.main()
