#! python3.10.4
# Start
# Design pattern number two -> abstract factory pattern
# Modules


class DiagramFactory:
    """ diagram builder from the scretch"""

    @classmethod
    def make_diagram(cls, width, height,):
        return cls.Diagram(cls, width, height)

    @classmethod
    def make_rectangle(cls, x, y, width, height, fill="white",
                       stroke="black"):
        return cls.Rectangle(x, y, width, height, fill, stroke)

    @classmethod
    def make_text(cls, x, y, text, fontsize=12):
        return cls.Text(x, y, text, fontsize)

    class Diagram:

        def __init__(self, width, height):
            self.width = width
            self.height = height


class SvgDiagramFactory(DiagramFactory):
    super().make_diagram()

    def make_diagram(self, width, height):
        return SvgDiagram(width, height)
        #
        #
        #
    def add(self, component):
        for y, row in enumerate(component.rows):
            for x, char in enumerate(row):
                self.diagram[y + component.y][x + component.x] = char

    SVG_SCALE = 20

    class SvgText:

        def __init__(self, x, y, text, fontsize):
            x *= self.SVG_SCALE
            y *= self.SVG_SCALE
            fontsize *= self.SVG_SCALE // 10
            self.svg = self.SVG_TEXT.format(**locals())

    class Text:
        """ abillity to change the cursor of the text plain
        and etc. """

        def __init__(self, x, y, text, fontsize):
            self.x = SvgDiagramFactory.SVG_SCALE
            self.y = SvgDiagramFactory.SVG_SCALE 
            fontsize *= SvgDiagramFactory.SVG_SCALE // 10


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

pashamk = SvgDiagramFactory.make_rectangle
# End
