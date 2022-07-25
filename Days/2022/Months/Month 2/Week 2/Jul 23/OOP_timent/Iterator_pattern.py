#!/usr/bin/python
# Start
# Exmplaes Using Iterator Pattern; It clearly explains iteration and
# the two protocols in question, but we'll be looking at several more
# readable ways to get this effect late ###

# Moduels
from collections.abc import Iterator



class CapitalIterable:
    """ Shows the base iteration """

    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return CapitalIterator(self.string)
    

class CapitalIterator:
    """ does all the operations and its kinds of
    stuff """

    def __init__(self, string:str):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0
    
    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()
    
        words = self.words[self.index]
        self.index += 1
        return words
    
    def __iter__(self):
        return self
        


# End