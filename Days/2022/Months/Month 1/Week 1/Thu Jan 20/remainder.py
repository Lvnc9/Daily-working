#! python3.9.9
# Start
# A Reminder to the old Thaught OOPs things :)
# TODO: Modules
from collections.abc import Container
from collections import namedtuple

# Chapter 5 < an short reminder from what we have learned and trained yesturday:
""" blobl blob la the end has came to the trueth xD """

class SingletonObject(object):
    
    class __SingletonObject:
        def __init__(self):
            self.val = None

        def __str__(self):
            return f"{self!r} {self.val}"
    
    instance = None

    def __new__(cls):
        if not SingletonObject.instance:
            SingletonObject.instance = SingletonObject.__SingletonObject()
        
        return SingletonObject.instance
    
    def __getattr__(self, name):
        return getattr(self.instance, name)
    
    def __setattr__(self, name):
        return setattr(self.instance, name)


Stock = namedtuple("Stock", "Current Highest Lowest Balance")
stock = Stock(21, 500, -23, 46)
print(stock)
# END