#!/usr/bin/python
# Start
### This time we make a class that can be composite 
# and concomposite at the same time
# Modules
from abc import ABCMeta

class Item:
    """ Can be composite and noncomposite at the same time """

    def __init__(self, name, price=0.00, *items):
        self.name = name
        self.price = price
        self.children = []

        if items:
            self.add(*items)
    
    @classmethod
    def create(cls, name, price):
        return Item(name, price=price)
    
    @classmethod
    def compose(cls, name, *items):
        return Item(name, *items)

    @property
    def composite(self):
        return bool(self.children)
        


# End