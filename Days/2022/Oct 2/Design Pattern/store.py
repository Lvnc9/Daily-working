#!/usr/bin/python
# Start
# Working on the store part of the shop project
# Module
import collections
import pstats


class Error: pass

class Order:
    """ will order products and list them to a dictionary
    and rate them as the number of times they are gotten ordered """

    pass


class Observer:
    
    @classmethod
    def rate(cls):
        pass

    @classmethod
    def order(cls, ProductName):
        pass
    
    
    def limit(self, productName, max):
        if max:
            self.max = self.products[productName]




class Store(Observer):
    ACTIVE, DORMANT = collections.namedtuple("ACTIVE", "DORMANT")

    productId = 0

    def __init__(self):
        self.products = collections.defaultdict()
        self.state = Store.ACTIVE

    def add(self, productName:str):
        if not self.state == Store.ACTIVE:
            raise Error("NOT ACTIVATED")
        name = productName.lower().capitalize()
        self.products[name] += 1
        
    def remove(self, productName):
        if not self.state == Store.ACTIVE:
            raise Error("NOT ACTIVATED")





# End