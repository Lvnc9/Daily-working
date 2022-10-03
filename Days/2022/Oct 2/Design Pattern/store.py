#!/usr/bin/python
# Start
# Working on the store part of the shop project
# Module
import collections


class Error: pass

class Order:
    """ will order products and list them to a dictionary
    and rate them as the number of times they are gotten ordered """

    pass


class Observer:
    pass


class Store(Observer):
    ACTIVE, DORMANT = collections.namedtuple("Active", "DORMANT")

    productId = 0

    def __init__(self):
        self.products = collections.defaultdict()

    def add(self, productName:str):
        name = productName.lower().capitalize()
        if not productName in self.products:
            self.products[name] += 1
            





# End