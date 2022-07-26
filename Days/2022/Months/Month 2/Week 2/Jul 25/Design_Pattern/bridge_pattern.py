#!/usr/bin/python3
# Start
# Looking for Brdige pattern for gaining strength :/
# Data playing -> drawing charts as both graphical and textual 
# at the end BarRenderer plays as bridge
# Modules
from collections import ChainMap
from abc import ABCMeta
import Image
import tempfile
import os
import re


class BarCharter:

    def __init__(self, renderer):
        if not isinstance(renderer, BarRenderer):
            raise TypeError("Expected object of type BarRenderer, got {}".
                            format(type(renderer).__name__))
        self.__renderer = renderer

    def render(self, caption, pairs):
        maximum = max(value for _, value in pairs)
        self.__renderer.initialize(len(pairs), maximum)
        self.__renderer.draw_caption(caption)
        for name, value in pairs:
            self.__renderer.draw_bar(name, value)
        self.__renderer.finalize()


# Insted of using hard coded base class and methods we use decorator
class Qtrac:
    def has_methods(*methods):
        def decorator(Base):
            def __subclasshook__(cls, subclass):
                if cls is Base:
                    attributes = ChainMap(*(Superclass.__dict__
                                            for Superclass in subclass.__mro__))
                    if all(method in attributes for method in methods):
                        return True
                return NotImplemented
            Base.__subclasshook__ = classmethod(__subclasshook__)
            return Base
        return decorator


class TextBarRenderer:
    """ Rendering the text from and then get moves to BarRenderer
    and BarRenderer will its roll as abstract part of bridge pattern """

    def __init__(self, scalefactor=40):
        self.scalefactor = scalefactor

    def initialize(self, bars, maximum):
        assert bars > 0 and maximum > 0
        self.scale = self.scalefactor / maximum

    def draw_caption(self, caption):
        print("{0}: ^{2}}\n{1: ^{2}}".format(
            caption, "=" * len(caption), self.scalefactor))

    def draw_bar(self, name, value):
        print("{} {}".format("*" * int(value, self.scale)), name)

    def finalize(self):
        pass


class ImageBarRenderer:
    """ Renders the Image part of data showment """

    COLORS = [Image.color_for_name(name) for name in (
        "red", "green", "blue", "yellow", "magneta", "cyan")]

    def __init__(self, stepHeight=10, barWidth=30, barGap=2):
        self.stepHeight = stepHeight
        self.barWidth = barWidth
        self.barGap = barGap
    
    def initialize(self, bars, maximum):
        assert bars > 0 and maximum > 0
        self.index = 0
        color = Image.color_for_name("White")
        self.image = Image.image(bars * (self.barWidth + self.barGap),
        maximum * self.stepHeight, background=color)
    
    def draw_caption(self, caption):
        self.filename = os.path.join(tempfile.gettempdir(),
        re.sub(r"\W+", "_", caption) + ".xpm")

    def draw_bar(self, name, value):
        color = ImageBarRenderer.COLORS[self.index %
        len(ImageBarRenderer.COLORS)]
        width, height = self.image.size
        x0 = self.index * (self.barWidth + self.barGap)
        x1 = x0 + self.barWidth
        y0 = height - (value * self.stepHeight)
        y1 = height - 1
        self.image.rectangle(x0, y0, x1, y1, fill=color)
        self.index += 1

    def finalize(self): 
        self.image.save(self.filename)
        print("wrote", self.filename)



def main():
    pairs = (("Mon", 16), ("Tue", 17), ("Wed", 19), ("Thu", 22),
             ("Fri", 24), ("Sat", 21), ("Sun", 19))
    textBarCharter = BarCharter(TextBarRenderer())
    textBarCharter.render('forcast 6/8', pairs)
    imagebarCharter = BarCharter(ImageBarRenderer)
    imagebarCharter.render('focast 6/8', pairs)

# can be used as two versions ->

# Version 1:


class Barrenderer(Qtrac.has_methods):
    requeired_methods = {'Intialaize', 'draw_caption', 'draw_bar', 'finalize'}

# Version 2:


@Qtrac.has_methods('Intialaize', 'draw_caption', 'draw_bar', 'finalize')
class BarRenderer():
    pass


# End