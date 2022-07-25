#!/bin/usr/python
# Start
### Comperhension examples to see wheter 
# modify a list or a data stucture using len() or sum() removing 
# duplicated data and etc.###
# Moduels
import sys
from collections import namedtuple

#filename = sys.argv[1]
#
#with open(filename) as file:
#    header = file.readline().strip().split('\t')
#    contacts = [
#        dict(
#            zip(header, line.strip().split('\t'))
#            for line in file)
#    ]
#
#for contact in contacts:
#    print("email: {email} -- {last}, {first}".format(
#        **contact))
#
Book = namedtuple('Book', 'Author tlte genre')
books = [
    Book("Pratchett", "Nightwatch", "fantasy"),
    Book("Pratchett", "Thief Of Time", "fantasy"),
    Book("Le Guin", "The Dispossessed", "scifi"),
    Book("Le Guin", "A Wizard Of Earthsea", "fantasy"),
    Book("Turner", "The Thief", "fantasy"),
    Book("Phillips", "Preston Diamond", "western"),
    Book("Phillips", "Twice Upon A Time", "scifi"),
    ]

fantasy_authors = {
    b.Author for b in books if b.genre == 'fantasy'
}
print(fantasy_authors)


# End