#!/usr/bin/python3
"""Module"""


import unittest
from models.rectangle import Rectangle


class testsNumber0(unittest.TestCase):
    """Test of Base() for assigning
    automatically an ID exists"""
    def test_0(self):
        self.r1 = Rectangle(1, 2)
        self.assertEqual(self.r1.id, 14)
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.height, 2)
        self.r2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(self.r2.id, 5)
    def test_1(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
        
class TestsNumber1(unittest.TestCase):
    def test_0(self):
         self.r3 = Rectangle(3, 3)
         self.assertEqual(self.r3.area(), 9)
        
if __name__ == '__main__':
    unittest.main()
