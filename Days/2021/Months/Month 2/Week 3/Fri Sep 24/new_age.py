#! python3.9.2
# Start
# Backing to the age of time when i was using the python and had a greate programming mind
# TODO: Modules
import os
from collections import namedtuple
def cleaning():
    os.system("clear")

cleaning()
test = 1, 2, 3, 4
print(type(test))

# Creating a tuple that is clear what members it has
stock = namedtuple("Stock", "Symbol Current High Low")
stock = stock("$", 34, 49, 20)
print(type(stock))

"The Idea is We Can use tuples as read only :)"

some_dict = {
    "name" : ("Sam", "Maria", "Loral"),
    "lname" : ("Mhmdi", "Corlos", "unknown"),
}

# Cleaning the table
cleaning()

# Showing the optional parameter that shows an error if the key not found
named_school = some_dict.get("namea", "NOT FOUND")

print(named_school)
# End