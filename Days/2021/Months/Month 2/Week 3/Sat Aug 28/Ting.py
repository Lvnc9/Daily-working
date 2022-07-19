#! python3.9.2
# Start
# Talk about the power of tuples and data structures
# Modules
from collections import namedtuple
import os

Stock = namedtuple('Stock', "symbol current high low")
stock = Stock('$', 43, 50, 30)
print(stock)

print(stock.high)

class Test(object):
    """ Testing the truth that all the attributes and
    methods are values of the dictioneries """

    def __init__(self, name, lname):
        self.name = name
        self. lname = lname
    
    def lil(self):
        print("Give me a truth x)")

print(Test.__dict__)

# Cleaning the hole screen
os.system("clear")
test = {
    "Google" : ("613", "625.86", "610"),
    "MSFT" : ("39.25", "59", "30")
}

test.setdefault("Google", "131")
print(test.get('Google'))
# End