#!/usr/bin/python3
"""Module"""
from models.base import Base


class Rectangle(Base):
    """Class rectangle inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) != int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if type(height) != int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        if type(x) != int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        if type(y) != int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """Returns the area of the rectangle"""
        return self.height * self.width

    def display(self):
        """Prints the rectangle in stdout"""
        print('\n' * self.y, end='')
        for _ in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        id = self.id
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        return f'[Rectangle] ({id}) {x}/{y} - {width}/{height}'

    def update(self, *args):
        """Update class"""
        for i in range(len(args)):
            if (i == 0):
                self.id = args[0]
            elif (i == 1):
                self.width = args[1]
            elif (i == 2):
                self.height = args[2]
            elif(i == 3):
                self.x = args[3]
            elif (i == 4):
                self.y = args[4]
            else:
                break
