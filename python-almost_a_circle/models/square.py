#!/usr/bin/python3
"""Module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        id = self.id
        x = self.x
        y = self.y
        height = self.height
        return f'[Square] ({id}) {x}/{y} - {height}'

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, size):
        self.width = size
        self.width = size

    def update(self, *args, **kwargs):
        """Update function"""
        if len(args) == 0:
            for i in kwargs:
                if i == 'id':
                    self.id = kwargs[i]
                if i == 'x':
                    self.x = kwargs[i]
                if i == 'y':
                    self.y = kwargs[i]
                if i == 'size':
                    self.height = kwargs[i]
                    self.width = kwargs[i]
            return
        for i in range(len(args)):
            if (i == 0):
                self.id = args[0]
            elif (i == 1):
                self.width = args[1]
                self.height = args[1]
            elif(i == 2):
                self.x = args[2]
            elif (i == 3):
                self.y = args[3]
            else:
                break

    def to_dictionary(self):
        """Class to dictionary function"""
        id = self.id
        size = self.width
        x = self.x
        y = self.y
        return {'id': id, 'size': size, 'x': x, 'y': y}
