#! python3.9.9
# Start
# THinking how lists can be usefull?; Maybe??;
# Modules
from collections import namedtuple
from collections import defaultdict
from collections import Counter

# What are lists, Hah?
class TestObject:
    """ Idk just working for some 
    damnly instantiation """

    def __init__(self, string):
        self.string = string

    def __str__(self):
        print("Hallo")
    
    def __repr__(self):
        return "Hallo"
a = TestObject('s')
b = TestObject('d')
c = TestObject('e')
lister = [a, b, c]

print(lister)


# Using __lt__ .ie less then 
class WeirdSortee:
    """ Show how to use .sort() of list data
    stracture and __repr__ """

    def __init__(self, string, number, sort_num):
        self.string = string 
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string
    
    def __repr__(self):
        return f"{self.string}:{self.number}"

class SomeOtherSortee:
    """ Training for sorting objects or its instantiatio """
    
    def __init__(self, string:str, number:int, num_sort:bool):
        self.string = string
        self.number = number
        self.num_sort = num_sort
    
    def __lt__(self, object):       # OR ANY GOD DAMN THING THAT YOU WISHED A TIME BEFORE xD
        
        return self.string < object.string

    def __repr__(self):
        return f"{self.string}:{self.number}"
t1 = SomeOtherSortee('ab', 3, False)
t2 = SomeOtherSortee('cd', 4, False)
t3 = SomeOtherSortee("ef", 1, False)

core = [t1, t2, t3]
core.sort()
print(core)

print(t1)
# End