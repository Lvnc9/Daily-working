#! python3.9.9
#Start 
# New Chapter Arrives Chpater 6:
# Modules
from collections import namedtuple

hand = ('pen', 'dashboard', 'teacher', 'desk')
print(type(hand))

test_dict = {
    (
        "Mom",
        "Dad",
        "Son",
        "Daughter") : "Mouse"

}

Stock = namedtuple("Stock", "Currency High Low Balance")
stock = Stock(432, 4234, 40, 3021)
print(stock.Currency)

# End