#! python3.9.2
# Start
# Talking about the new chapter of the book OOP
# TODO Modules
from collections import namedtuple

class Test(object):
    """ Some test class for showing the power of
    the __slots__ function for reducing the amount of code
    for arbitrary attributes """

    __slots__=['pashmak', 'name']
    def __init__(self, *args, **kwargs):
        self.pashmak = 2
        self.name = "Sam"

tuple1 = "FB", 75.00, 75.03, 74.90
tuple2 = ("FB", 75.00, 75.03, 74.90)
print('Without pranteses:\t', tuple1, '\nWith paranteses:\t', tuple2)

Stock = namedtuple("Stock", "symbol current high low")
stock = Stock("FB", 32, 35, 29)

print(stock.high)

# End