#! python3.9.9
# Start
# Look back to the old Thaught things of OOP
#  Some Notes before goind to write wholl .py file: 
#    Deletion function in property using is :
#      Logging
#      veto

# TODO: Modules
from collections.abc import Container
from sqlite3 import converters

from numpy import delete

class Information(object):
    """ As we know im not using the keyboard for that much
    programming yet and it is bothering me ofcourse but i'll
    back soon; i promise xD 
    stranage but the mosules of my hand are getting hurted
    thats cool; i hadn't this kind of injurness
    but of course this is happening becouse that was a long time ago
    of me being a real programming student 
    DAMN """
    def __init__(self, name:str, fname:str):
        self.__name = name
        self.__fname = fname

    @property
    def converter(self):
        print('Showing converted name:')
        return self.__converted_name
    
    @converter.setter
    def converter(self, converted_name:str):
        print(f'The value has changed successfully to {self.__converted_name}')
        self.__converted_name = converted_name

    @converter.deleter
    def converter(self, veto:str):
        print(f"YOU ARE DELETING {self.converter} property")
        print("ARE YOU CERTAIN OF DOING THAT?")
        ans = str(input().lower())
        if ans[0] == 'y':
            del self.converter
        else:
            print("NOT DELETED")

def reader(inthe:str):
    num = 0
    for number in inthe:
        if '=' == number:
            num += 1
        else :
            pass
    print(num)
reader('=============  Sum : 3:00"H  =============')
print(len('- - - - - - - - - - - - - - -'))
# End 