#!/usr/bin/python
# Start
# Using iterator pattern for accecing data and files without exposing
# to its collection or aggregate
# Module

# Implementing sequence protocol
class AtoZ:

    def __getitem__(self, index):
        if 0 <= index < 26:
            return chr(index + ord("A"))
        raise IndexError()


for item in AtoZ():
    print(item, end="")
print()


# Implementition for Iter function
class Presidents:
    """ Iterating over the presidents of US
    Simple usage just Iterate over the object """

    __name = ("George Washington",
              "John Adams",
              "Thomas Jefferson",
              "Bill Clinton", 
              "George W. Bush", 
              "Barack Obama")

    def __init__(self, first=None):
        self.index = (-1 if first is None else
                      Presidents.__name.index(first) - 1)
    
    def __call__(self):
        self.index += 1
        if self.index < len(Presidents.__name):
            return Presidents.__name[self.index]
        raise StopIteration()

for pres in iter(Presidents('George Washington'), "Georg W. Bush"):
    print(pres, end="")

# implementing __iter__
class Bag:
    """ __iter__ had been implemented for counting 
    the times the items had been inserted into the self.items """

    def __init__(self, items=None):
        self.__bag = {}
        if items is not None:
            for item in items:
                self.add(item)
        
    def add(self, item):
        self.__bag[item] = self.__bag.get(item, 0) + 1
    
    def __delitem__(self, item):
        if self.__bag[item] is not None:
            self.__bag[item] -= 1
            if self.__bag[item] <= 0:
                del self.__bag[item]
        else:
            raise KeyError(str(item))
    
    def count(self, item):
        return self.__bag.get(item, 0)
    
    def __contains__(self, item):
        return item in self.__bag
    
    def __len__(self):
        return sum(count for count in self.__bag.values())
    
    def __iter__(self):
        for item, count in self.__bag.items():
            for _ in range(count):
                yield item

# End