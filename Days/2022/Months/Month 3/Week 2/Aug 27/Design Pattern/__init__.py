#!/usr/bin/python
# Start
# Manipulating an Image creational file
# Modules
import os
import importlib
import warnings


# Checking numpy
try:
    import numpy
except ImportError:
    numpy = None
    import array



# Walking through the current directory and checking for all the images
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


class Error(Exception): pass


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
    

# End