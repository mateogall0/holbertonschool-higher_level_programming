#!/usr/bin/python3
"""Module"""


import unittest
from models.rectangle import Rectangle


class testsNumber0(unittest.TestCase):
    """Test of Base() for assigning
    automatically an ID exists"""
    def test_0(self):
        self.assertEqual(Rectangle(1, 2).id, 13)

if __name__ == '__main__':
    unittest.main()
