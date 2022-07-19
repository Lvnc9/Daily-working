#! python3.9.9
# Start
# Talking about data structures and this kind of things you know :)
# Modules
from collections import namedtuple
from collections import defaultdict
from collections import Counter
from functools import total_ordering

# List kinds of things that we want to discuss :)

@total_ordering
class WeirdSortee:
    """ How to sort objects in a list Han?
    well we can do this with the trick and the built in
    functions that we are about to use """

    def __init__(self, string:str, number:int, sort_num:bool):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string

    def __eq__(self, object):
        return all((
            self.string == object.string,
            self.number == object.number,
            self.sort_num == object.sort_num
        ))

    def __repr__(self):
        return f"{self.string}:{self.number}"

t1 = WeirdSortee('w', 2, True)
t2 = WeirdSortee('e', 1, True)
t3 = WeirdSortee('a', 3, True)
finall = [t1, t2, t3]
finall.sort()
print(finall)
for i in finall:
    i.sort_num = False

finall.sort()
print("Alphabetical version")
print(finall)
# End