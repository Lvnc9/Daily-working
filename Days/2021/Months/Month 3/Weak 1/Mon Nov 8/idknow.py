#! python3.9.2
# Start
# Loocking back to the old thought codes (:1
# Modules
from collections.abc import Container
from urllib.request import urlopen
import time

class SomeTest(object):
    """ As lil mana who knows how to use propertys
    i will use it properly, I Swear it to the prorgramm
    anciant :z """

    def __init__(self, url:str):
        self.url = url
        self.__content = None
    
    @property
    def content(self):
        if not self.__content:
            self.__content = urlopen(self.url).read()
        
        return self.__content

class Lister(list):
    """ take an class as input and 
    return the average value of the list  """

    @property
    def average(self):
        print(f"The average Value of {self}:")
        return sum(self) / len(self)

lil = Lister([1, 2, 3, 4, 5])
print(lil.average)
# End