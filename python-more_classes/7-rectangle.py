#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if type(height) != int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        if type(width) != int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        s = ''
        if self.height == 0 or self.width == 0:
            return s
        for i in range(self.height):
            for _ in range(self.width):
                s += str(self.print_symbol)
            if i != self.height - 1:
                s += '\n'
        return s

    def __repr__(self):
        w = str(self.width)
        h = str(self.height)
        return 'Rectangle(' + w + ', ' + h + ')'

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
