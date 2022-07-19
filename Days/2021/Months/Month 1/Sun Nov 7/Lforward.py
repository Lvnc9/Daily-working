#! python3.9.2
# Start
# Talking back to the old codes of the chapter 5 of OOP
# Modules
from urllib.request import urlopen
import os 

class AnotherTest(object):
    """ Testing property function but this time
    with decorators """

    def __init__(self, name:str, fname:str):
        self._name = name
        self._fname = fname
    
    @property
    def cheker(self):
        return self._name
    
    @cheker.setter
    def cheker(self, name):
        if not len(name) >= 2:
                raise Exception("PLeas Enter A Valid Name")
        
        self._name = name
        print(f"You have set the attribute to {self._name}")

    @cheker.deleter
    def cheker(self):
        ans = str(input("Are You Sure For Deleting this Attr? [y/n]\n"))
        if 'y' in ans:
            del self._name
    
lil = AnotherTest("Sam", "Mohammadi")
lil.cheker = 'idk'


class WebPage(object):
    """ Testing the usage of the property attrs """

    def __init__(self, url:str):
        self._url = url
        self._content = None
    
    @property
    def content(self):
        if not self._content:
            print(f"Retrieving the new page...")
            self._content = urlopen(self._url).read()

        return self._content

class AverageList(list):
    """ Get an list and return it with the average value
    of the list """

    @property
    def averager(self):
        os.system('clear')
        print("the Average Value of the list:\n")
        return sum(self) / len(self)

a = AverageList([1, 2, 3, 4, 5, 6, 7])
print(a.averager)
# End