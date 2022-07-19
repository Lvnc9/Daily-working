#! python3.10.4
# Start
# learning new patterns including Singleton, prototype
# Modules
""" Not Imported Yet """

import copy


class Point:
    """ sample of prototyping class """
    
    __slots__ = ("y", "x")

    def __init__(self, x, y):
        self.x = x
        self.y = y

point1 = copy.deepcopy(Point)
print(point1)
point1.x = 1
point1.y = 2
print(point1.x, point1.y)


# End