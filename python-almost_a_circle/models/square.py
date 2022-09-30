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
        width = self.width
        height = self.height
        return f'[Square] ({id}) {x}/{y} - {width}/{height}'
