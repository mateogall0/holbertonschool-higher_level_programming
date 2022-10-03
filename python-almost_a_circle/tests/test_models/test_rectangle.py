#!/usr/bin/python3
"""Module"""


import unittest
from models.base import Base


class testsNumber0(unittest.TestCase):
    """Test of Base() for assigning
    automatically an ID exists"""
    def test_0(self):
        self.assertEqual(Rectangle().id, 1)

if __name__ == '__main__':
    unittest.main()
