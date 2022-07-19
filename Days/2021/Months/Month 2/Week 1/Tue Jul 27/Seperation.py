#! python 3.9.2
# Start
# Understanding where to use OOP and classes and where to not use

class Polygon:
    def __init__(self):
        self.vertices = []
    
    def __init__(self, points=None):
        points = points if points else []
        self.vertices = []
        for point in points:
            if isinstance(points, tuple):
                point = Point(*point)

    def add_point(self, point):
        self.vertices.append((point))

    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
            return perimeter



class Color:
    def __init__(self, rgb_value, name):
        self._rgb_value = rgb_value
        self._name = name
    
    # Old #def set_name(self, name):
    # Old #    self._name = name

    def set_name(self, name):
        if not name:
            raise Exception("invalid Name")
        self._name = name

    def get_name(self):
        return self._name

class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name
    
    def _set_name(self, name):
        if not name:
            raise Exception("""Oops!
            looks like someone tryed to give an invalid Name!""")
    
    def _get_name(self):
        return self._name

    name = property(_get_name, _set_name)

pashmak = Color("#0000ff", "bright red")
pashmak.name = ""

# End