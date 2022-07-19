#! python3.9.9
# Start
# Works on the finding the best situation for using what data structure
# Modules
from collections import namedtuple, defaultdict, Counter
from functools import total_ordering
from operator import itemgetter, attrgetter, methodcaller
import os
import time
import shutil 
import pathlib
from pathlib import Path
import glob

from cairo import Path

class IdkWhen(set):
    """ Don't really know yet to what to do with this class
    but as the Mr.marting Thought me i have to block out the
    class when ever i want to do something """
    pass

    def __init__(self, t1:set, t2:set):
        self.t1 = t1
        self.t2 = t2
    
    def __str__(self):
        return "Accepts to attributes for interacting with eachother"

test_n_1 = IdkWhen({1, 2, 3,}, {1, 2, 3, 4, 5})
print(test_n_1.t1.symmetric_difference(test_n_1.t2))

os.system("clear")

shaming = "Earth"
shaming1 = "Circle"
print(shaming is shaming1)
time.sleep(1)

# All this part does is to just recovert the old information of pathlib we have lost


pathi = pathlib.Path.home() / "Movies" / 
print(pathi) 
# End