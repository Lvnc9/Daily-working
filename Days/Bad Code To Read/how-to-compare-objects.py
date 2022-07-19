#!python3.9.9
# Start
### The base shape of the objects that can be compared with
#sort() list functions###
# Modules
from functools import total_ordering

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


# End
