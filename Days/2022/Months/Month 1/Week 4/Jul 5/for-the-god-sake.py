#! python3.10.4
# Start
# design patterns and this kine of stuffs
# yea###
# Modules
import socket
import os
from 
from matplotlib.patches import Rectangle
# Nothing new of being devocated
# but what is getting devocated?
# we dont know! :) ###
# as we start


class DiagramFactory:
    """ diagram builder from the scretch"""

    def make_diagram(self, width, height,):
        return Diagram(width, height)

    def make_rectangle(self, x, y, width, height, fill="white",
                       stroke="black"):
        return (x, y, width, height, fill, stroke)

    def make_text(self, x, y, text, fontsize=12):
        return Text(x, y, text, fontsize)


class SvgDiagramFactory(DiagramFactory):
    super().make_diagram()

    def make_diagram(self, width, height):
        return SvgDiagram(width, height)
        #
        #
        #


class Text:
    """ abillity to change the cursor of the text plain
    and etc. """

    def __init__(self, x, y, text, fontsize):
        self.x = x
        self.y = y
        self.rows = [list[text]]


class Diagram:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def add(self, component):
        for y, row in enumerate(component.rows):
            for x, char in enumerate(row):
                self.diagram[y + component.y][x + component.x] = char
                
SVG_SCALE = 20
class SvgText:

    def __init__(self, x, y, text, fontsize):
        x *= SVG_SCALE
        y *= SVG_SCALE
        fontsize *= SVG_SCALE // 10
        self.svg = SVG_TEXT.format(**locals())


def create_diagram(factory):
    diagram = factory.make_diagram(30, 7)
    rectangle = factory.make_rectangle(4, 1, 22, 5, "yellow")
    text = factory.make_text(7, 3, "Abstract Factory")
    diagram.add(rectangle)
    diagram.add(text)
    return diagram


def main():
    "What we add later"

    textDiagram = create_diagram(DiagramFactory())
    textDiagram.save(textFilename)

    svgDiagram = create_diagram(SvgDiagramFactory)
    svgDiagram.save(svgFilename)

# End
