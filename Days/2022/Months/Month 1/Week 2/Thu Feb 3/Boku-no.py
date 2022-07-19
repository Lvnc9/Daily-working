#! python3.9.9
# Start
# Talking about data structores and this kind of stuff
# Modules
from collections import namedtuple, defaultdict, Counter
from functools import total_ordering
from operator import itemgetter, attrgetter, methodcaller
import time
import os

@total_ordering
class WeirdSortee:    
    """ A class that can be sorted in a list
    with other types of objects to become a compareble
    object """

    def __init__(self, string:str, number:int, sort_num:bool):
        self.string = string
        self.number = number
        self.sort_num = sort_num
    
    def __lt__(self, object):
        if self.sort_num:
            return self.number < object.number
        return object.string < object.string
    
    def __eq__(self, object):
        return all((
            self.string == object.string,
            self.number == object.number,
            self.sort_num == object.number
        ))

    def __repr__(self):
        return f"{self.string}:{self.number}"

class WithoutFunctions:    
    """ A class that can be sorted in a list
    with other types of objects to become a compareble
    object """

    def __init__(self, string:str, number:int, sort_num:bool):
        self.string = string
        self.number = number
        self.sort_num = sort_num
    
    def __repr__(self):
        return f"{self.string}:{self.number}"

# Instanse of operator less object
wftest = WithoutFunctions('z', 2, True)
wftest2 = WithoutFunctions('w', 1, True)
wftest3 = WithoutFunctions('a', 10, True)

# Lists of objects
lil_test = [(5, 10, 23), (4, 13, 21), (1, 0, 25)]
wfHolder = [wftest, wftest2, wftest]


# Showing Results
lil_test.sort(key=itemgetter(2))
print(lil_test)


tasty_set = {1, 2, 3, 4}

# Trying to add some items to a set data Structures 
Songs = [("idk", "you DK"),
        ("Solic", "Solic House"),
        ("Pashmak", "Lil ones"),
        ("And", "Some Goodie")
        ]

Artists = set()
for song, artist in Songs:
    Artists.add(artist)
    os.system("clear")
    print(Artists)

    time.sleep(1)
print("done")

# End