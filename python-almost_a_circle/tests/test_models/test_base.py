#!/usr/bin/python3
"""Module"""


import unittest
from models.base import Base


class TestStringMethods(unittest.TestCase):
    """Test String Methods"""
    def t0(self):
        o = Base()
        self.assertEqual(o.id, 1)

if __name__ == '__main__':
    unittest.main()
