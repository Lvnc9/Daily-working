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

# End