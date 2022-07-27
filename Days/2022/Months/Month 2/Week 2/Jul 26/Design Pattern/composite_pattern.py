#!/usr/bin/python
# Start
# Design pattern again
# Modules
from abc import ABCMeta, abstractproperty
from sys import stdout


def main():
    pencil = SimpleItem("Pencil", 0.40)
    ruler = SimpleItem("Ruler", 1.60)
    eraser = SimpleItem("Eraser", 0.20)
    pencilSet = CompositeItem("Pencil Set", pencil, ruler, eraser)
    box = SimpleItem("Box", 1.00)
    boxedPencilSet = CompositeItem("Boxed Pencil Set", box, pencilSet)
    boxedPencilSet.add(pencil)
    for item in (pencil, ruler, eraser, pencilSet, boxedPencilSet):
        item.print()

class AbstractItem(ABCMeta):

    @abstractproperty
    def composite(self):
        pass
    
    def __iter__(self):
        return iter([])

class SimpleItem(AbstractItem):
    
    def __init__(self, name:str, price=0.00):
        self.name = name
        self.price = price
    
    def composite(self):
        return False

    def print(self, indent="", file=stdout):
        print("{}${:2f} {}".format(indent, self.price, self.name), file=file)


class AbstractCompositeItem(AbstractItem):

    def __init__(self, *items):
        self.children = [] 
        if items:
            self.add(*items)
    
    def add(self, first, *items):
        self.children.append(first)
        if items:
            self.children.extend(items)
    
    def remove(self, item):
        self.children.remove(item)
    
    def __iter__(self):
        return iter(self.children)
    
class CompositeItem(AbstractCompositeItem):

    def __init__(self, name, *items):
        super().__init__(*items)
        self.name = name
    
    def composite(self):
        return True

    @property
    def price(self):
        ### Its like a generator!, we can loop over 
        # the subclass and the super classes ###
        return sum(item.price for item in self)
    
    def print(self, indent='', file=stdout):
        print("{}${:.2f}{}".format(indent, self.price, self.name), file=file)
        for child in self:
            child.print(indent + "      ")

# End