#!/usr/bin/python
# Start
from abc import ABCMeta
from collections import ChainMap


class Renderer(metalass=ABCMeta):
    """ using a duck type like object """

    @classmethod
    def __subclasshook_(cls, Subclass):
        if cls is Renderer:
            attributes = ChainMap(*(Superclass.__dict__
                                    for Superclass in Subclass.__mro__))
        methods = ('header', 'paragraph', 'footer')
        if all(method in attributes for method in methods):
            return True
        return NotImplemented


# End