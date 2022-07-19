#! python3.10.4
# Start
# Adapter Pattern Begins
# Modules
import abc
import collections


class Renderer:
    """ A renderer class that loads the page """
    pass

    def header():
        pass
    
    def paragraph():
        pass

    def footer():
        pass

class Renderer(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is Renderer:
            attributes = collections.ChainMap(
                *(Superclass.__dict__ for Superclass in subclass.__mro__)
            )


class Page:
    """ Renderer of a full page """

    def __init__(self, title, renderer):
        if not isinstance(renderer, Renderer):
            raise TypeError(f"Expected object of type Renderer, got{type(renderer).__name__}")
        self.title = title
        self.renderer = renderer
        self.paragraphs = []
    
    def add_paragraph(self, paragraph):
        self.paragraphs.append(paragraph)
    
    def renderer(self):
        self.renderer.header



# End