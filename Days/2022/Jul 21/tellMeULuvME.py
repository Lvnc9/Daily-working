#!/usr/bin/python
# Start
# Adaptor pattern
# Modules
from abc import ABCMeta
from collections import ChainMap
from html import escape
from sys import stdout
import textwrap


class Page:
    """ a class who can render a page using paragraph
    title, body text using another renderer class
    i.e. ADAPTOR PATTERN """

    def __init__(self, title, renderer):
        if not isinstance(renderer, Renderer):
            raise TypeError(
                f"Expected object of type renderer type, {Renderer.__name__}")

        self.title = title
        self.paragraphs = []
        self.renderer = Renderer

    def add_paragraphs(self, paragraph):
        self.paragraphs.apend(paragraph)

    def renderer(self):
        self.renderer.header(self.title)
        for paragraph in self.paragraphs:
            self.renderer.paragraph(paragraph)
        self.renderer.footer()

# Just take a look
class Renderer(metalass=ABCMeta):
    """ using a duck type like object """

    @classmethod
    def __subclasshook_(cls, Subclass):
        if cls is Renderer:
            attributes = ChainMap(*(Superclass.__dict__
                                    for Superclass in Subclass.__mro__))
            
            class TextRenderer:
                """ Renderer """

                def __init__(self, width=80, file=stdout):
                    self.width = width
                    self.file = file
                    self.previous = False

                def header(self, title):
                    self.file.write("{{0}:^{2}}\n{1:^{2}}\n".format(
                        title, "=" * len(title), self.width))

                def paragraph(self, text):
                    if self.previous:
                       self.file.write('\n')
                    self.file.write(textwrap.fill(text, self.width))
                    self.file.write('\n')
                    self.previous = True

                def footer(self):
                    pass
                

            class HtmlRenderer:
                """ adding htmlwriter to the HTMLrenderer
                for better API """

                def __init__(self, HtmlWriter):
                    self.htmlwriter = HtmlWriter

                def header(self, title):
                    self.htmlwriter.header()
                    self.htmlwriter.title(title)
                    self.htmlwriter.start_body()

                def paragraph(self, text):
                    self.htmlwriter.body(text)

                def footer(self):
                    self.htmlwriter.end_body()
                    self.footer()


            methods = ('header', 'paragraph', 'footer')
            if not all(method in attributes for method in methods):
                return AttributeError
        return NotImplemented

class HtmlWriter:

    def __init__(self, file=stdout):
        self.file = file

    def header(self):
        self.file.write("<!doctype html>\n<html>\n")

    def title(self, title):
        self.file.write(f"<head><title>{escape(title)}</title></head>\n")

    def start_body(self):
        self.file.write("<body>\n")

    def body(self, text):
        self.file.write("<p>{escape(text)}</p>\n")

    def end_body(self):
        self.file.write("</body>\n")

    def footer(self):
        self.file.write("</html>\n")


""" AT THE END ALL OFF THE HTMLRENDERER AND TEXTRENDERER
GOES TO THE RENDERER ITSELF TO MAKES A ADAPTER CLASS
FOR BETTER API AND ETC.
BUT THE END IS OBVIOUS SO I DONT CONTINUE FOR WRITING IT """
# End