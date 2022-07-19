#! python3.9.9
# Start
# A bit of loocking back to how to use OOP And than back to the main chapater and continuing
# TODO: Modules
from collections.abc import Container

class some_test(object):
    """ Showing the deletation abillity """

    def __init__(self, name:str):
        self.name = name 

    @property
    def somehow(self):
        return self.__name
    
    @somehow.setter
    def somehow(self, name:str):
        print(f"you are saving {name}")
        self.__name = name

lil = some_test('idk')
lil.somehow = 'idk'
lil.fsdfd = 1
and_some_other_test = (1, 1)
print(and_some_other_test)
and well that is not equal as the lighy is 


class Same_hood(object):
    """ well Try to show somehting different from the others xD """
    def __init__(self, k_b_name:str='', owner:str=''):
        self.k_b_name = k_b_name
        self.owner = owner 
    
    def action(self):
        print(self.k_b_name)
    
# End