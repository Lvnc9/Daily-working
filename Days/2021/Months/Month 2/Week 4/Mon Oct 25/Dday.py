#! python3.9.2
# Start
### training the old stuff we worked together for growing 
# and getting back to the road #
# Modules
from collections.abc import Container
import abc
import math

# Making a silly odd number finder

class OddFinder(Container):
    "Shell find the odd numbers"

    def __contains__(self, x):
        # odd numbers % 2, always have remainders 
        if not isinstance(x, int) or not x % 2:
            return False
        
        return True

class MediaLoader(abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractproperty
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        """ Check if :
        method was called in on this class rather than another class.
        all the abstract methods are suplied in the conditated class
         """
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        
        return NotImplemented 


class Point:
    """ Represent the Points and saves them """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        return math.squrt((self.x - p2.x)**2 + (self.y - p2.y)**2)

class Polygon:
    """ Create the pollygon with the tooken points """

    def __init__(self, points=None):
        self.points = points if points else []
        self.vertices = []
        
        for point in points:
            if isinstance(point, tuple):
                point = Point(*point)
            self.vertices.append(point)
    
    def add_point(self, point):
        self.vertices.append(point)
    
    def perimiter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        
        return perimeter
# End 