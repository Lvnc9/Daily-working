#!/usr/bin/python
# Start
### using __slots__ for memory reduction  ### 
# Modules
import shelve
import os
import tempfile
import atexit

class Point:
    """ Instance dont include __dict__ 
    and can not use arbitrary argumants like setting values
    
    Point.example = 'author' -> Error"""

    __slots__ = ('x', 'y', 'z', 'color')
    def __init__(self, x=0, y=0, z=0, color=None):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"exists at |{self.x}|\n\t  |{self.y}|\n\t  |{self.z}|"

lala = Point(2, 4, 5)
print(lala)


class Point:
    
    __slots__ = ()
    __dbm = shelve.open(os.path.join(tempfile.gettempdir, 'point.db'))

    def __init__(self, x=0, y=0, z=0, color=None):
        self.x = x
        self.y = y
        self.z = z
        self.color = color

    def __key(self, name):
        return f"{id(self):X}{self.name}"
    
    def __getattr__(self, name):
        return Point.__dbm[self.__key(name)]

    def __setattr__(self, name, value):
        self.__dbm[self.__key(name)] = value
    
    atexit.register()


# End