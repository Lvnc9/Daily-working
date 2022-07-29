#!/usr/bin/python
# Start
# Composite continues
# Modules

import itertools
from sys import stdout


class Item:
    def __init__(self, name, price=0.00, *items):
        self.name = name
        self.price = price
        self.children = []
        if items:
            self.add(*items)

    @classmethod
    def create(cls, name, price):
        return Item(name, price)
    
    @classmethod 
    def compose(cls, name, *items):
        return Item(name, *items)

    @property
    def composite(self):
        return bool(self.children)

    def add(self, first, *items):
        self.children.extend(itertools.chain((first), *items))

    def __iter__(self):
        return iter(self.children)

    @property
    def price(self):
        return (sum(item.price for item in self) if
        self.children else self.__price)
    
    @price.setter
    def price(self, price):
        self.__price = price

    def print(self, indent='', file=stdout):
        print("{}@{:2f} {}".format(indent, self.price, self.name), file=file)
        for child in self:
            child.print(indent, + "     ")

def make_item(name, price):
    return Item(name, price)

def make_composite(name, *items):
    return Item(name, *items)


# End