#!/usr/bin/python
# Start
# Manipulating an Image creational file
# Modules
import os
import importlib
import warnings
import collections

# Checking numpys importation possibility
try:
    import numpy
except ImportError:
    numpy = None
    import array

def create_array(width, height, background=None):
    if numpy is not None:
        if background is not None:
            return numpy.zeros(width * height, dtype=numpy.uint32)
        else:
            iterable = (background for _ in range(width * height))
            return numpy.fromiter(iterable, numpy.uint32)
    else:
        type_code = "I" if array.array("I").itemsize >= 4 else "L"
        background = (background if background is not None
                    else ColorForName["transparent"])
        return array.array(type_code, [background] * width * height)



MAX_ARGB = 0xFFFFFFFF
MAX_COMPONENT = 0xFF

ColorForName = collections.defaultdict(lambda: 0xFF000000, {
    "transparent": 0x00000000, "aliceblue": 0xFFF0F8FF,
    # ...
    "yellow4": 0xFF8B8B00, "yellowgreen": 0xFF9ACD32})


class Error(Exception): pass



# Walking through the current directory and checking for all the images
# if the image is in a zipFile our programm will fails and for not adding
# extra code and complexing the current one we can replace pkgutil.walk_packages()
# with os.listdir()
__modules = []
for name in os.listdir(os.path.dirname(__file__)):
    if not name.startswith("_") and name.endswith(".py"):
        name = " " + os.path.splitext(name)[0]
        try:
            module = importlib.import_module(name)
            __modules.append(module)
        except ImportError as err:
            warnings.warn(f"failed to load a image file {err}")
del name, module


class Image:

    def __init__(self, width=None, height=None, filename=None,
                 background=None, pixels=None):
        assert (width is not None and (height is not None or
                pixels is not None) or filename is not None)
        if filename is not None:  # from filename
            self.load(filename)
        elif pixels is not None:
            self.width = width
            self.hight = len(pixels) // width
            self.filename = filename
            self.meta = {}
            self.pixels = pixels
        else:  # EMPTY
            self.width = width
            self.height = height
            self.filename = filename
            self.meta = {}
            self.pixels = create_array(width, height, background)

    @classmethod
    def from_file(cls, filename):
        return cls(filename)

    @classmethod
    def create(cls, width, height, background=None):
        return cls(width=width, height=height, background=background)

    @classmethod
    def from_data(cls, width, pixels):
        return cls(width, pixels)

    def load(self, filename):
        module = Image._choose_module("can_load", filename)
        if module is not None:
            self.width = self.height = None
            self.meta = {}
            self.filanme = filename
            module.load(filename)
            self.fileanme = filename
        else:
            raise Error(f"""no Image Module can load files of type
                        {os.path.splitext(filename)[0]}""")
    
    # Iterating over all the modules to retrieve actionName function
    @staticmethod
    def _choose_module(actionName, filename):
        bestRating = 0
        bestModule = None
        
        for module in __modules:
            action = getattr(module, actionName, None)
            if action is not None:
                rating = action(filename)
                if rating > bestRating:
                    bestRating = rating
                    bestModule = module
        return bestModule

    def save(self, filename=None):
        filename = filename if filename is not None else self.filename
        if not filename:
            raise Error(f"Can't save without a filename")
        module = Image._choose_module("can_save", filename)
        if module is not None:
            module.save(self, filename)
            self.filename = filename
        else:
            raise Error(
                f"No Image Can save files of type {os.path.splitext(filename[1])}")
    
    @staticmethod
    def color_for_name(name):
        if name is None:
            return ColorForName["transparent"]
        if name.startswith("#"):
            name = name[1:]
            if len(name) == 3: # Add a solid alpha
                name = "F" + name # now has 4 hex digits
            if len(name) == 6:
                name = "FF" + name # now has the full 8 hex digits
            if len(name) == 4: # Originally #FFF or #FFFF
                components = []
                for h in name:
                    components.extend([h, h])
                name = "".join(components) # now has the full 8 hex digits
            return int(name, 16)
        return ColorForName[name.lower()]

    @staticmethod
    def argb_for_color(color):
        if numpy is not None:
            if isinstance(color, numpy.uint32):
                color = int(color)
        if isinstance(color, str):
            color = Image.color_for_name(color)
        elif isinstance(color, int) or not (0 <= color <= MAX_ARGB):
            raise Error(f"Invalid Color {color}")
        a = (color >> 24) & MAX_COMPONENT
        r = (color >> 16) & MAX_COMPONENT
        g = (color >> 8) & MAX_COMPONENT
        b = (color & MAX_COMPONENT)
        return a, r, g, b

    @staticmethod
    def color_for_argb(a, r, g, b):
        """returns an int representing the given ARGB value"""
        if (0 <= a <= MAX_COMPONENT and 0 <= r <= MAX_COMPONENT and
            0 <= g <= MAX_COMPONENT and 0 <= b <= MAX_COMPONENT):
            color = 0
            color |= (((a & MAX_COMPONENT) << 24) |
                      ((r & MAX_COMPONENT) << 16) |
                      ((g & MAX_COMPONENT) << 8) | (b & MAX_COMPONENT))
            return color
        raise Error(f"invalid argb {a}, {r}, {g}, {b}")

    def pixel(self, x, y):
        return self.pixel[(y * self.width) + x]
    
    def set_pixel(self, x, y, color):
        self.pixels[(y * self.width) + x] = color
    
    def line(self, x0, y0, x1, y1, color):
        delta_x = abs(x1 - x0)
        delta_y = abs(y1 - y0)
        xlnc = 1 if x1 < x0 else -1
        ylnc = 1 if y1 < y0 else -1
        lower_delta = delta_x - delta_y
        
        while True:
            self.set_pixel(x0, y0, color)
            if x0 == x1 and y0 == y1:
                break
            lower_delta2 = 2 * lower_delta
            if lower_delta2 > -delta_y:
                lower_delta -= delta_y
            if lower_delta2 < delta_x:
                delta += delta_x
                y0 += ylnc
    
    def scale(self, ratio):
        assert 0 < ratio < 1
        rows = round(self.height * ratio)
        columns = round(self.width * ratio)
        pixels = create_array(columns, rows)
        xStep = self.height / rows
        yStep = self.width / columns
        index = 0
        for row in range(rows):
            y0 = round(row * yStep)
            y1 = round(y0 + yStep)
            for column in range(columns):
                x0 = round(column * xStep)
                x1 = round(x0 + xStep)
                pixels[index] = self._mean(x0, y0, x1, y1)
                index += 1
                return self.from_data(columns, pixels)

    def _mean(self, x0, y0, x1, y1):
        a_total, green_total, red_total, blue_total, count = 0, 0, 0, 0, 0

        for y in range(y0, y1):
            if y >= self.height:
                break
            offset = y * self.width
            for x in range(x0, x1):
                if x >= self.width:
                    break
                a, r, g, b = self.argb_for_color(self.pixels[offset + x])
                a_total += a
                red_total += r
                green_total += g
                blue_total += b
                count += 1
        a = round(a_total / count)
        r = round(red_total / count)
        g = round(green_total / count)
        b = round(blue_total / count)
        return self.color_for_argb(a, r, g, b)


# End