# Start
# Chapter 6 Arrives in Air time to have some bully molly
# Modules
from collections import namedtuple
from collections.abc import Container
import pprint

# Reminder 

class DictTalk(object):
    """ Look Through dictionarie attributes and
    properties for a Biger picture """
    def __init__(self):
        self.House = namedtuple("House", "Leftside Rightside Upside Downside")
        self.Room = namedtuple('Room', "Wallpaper PinsColor PC MusicStyle")
        self.room = self.Room("Animes", "Silver", "Old-Good", "Lo-FI")
        self.leader_ship = {
            "Familly" : ("Alderson", 'manlyhan', 'Timberson'),
            "Citys" : ("New York", "Washington", "Pencilwania"),
            "Pets" : ("Dogs", "Cats", "Birds", "Monkeys", "Savage Animals"),
        }
        self.major_two = {
            self.House("")
        }

    def Shower(self, att1:object):
        if att1 == self.room:
            print(f"This is {att1.__doc__}")
            return att1.Wallpaper
        try:
            print('shit')

        except ZeroDivisionError:
            print("Why the Hell you'r dividing something to 0 :\\")

        finally:
            print("This happends Anyway")

        print(self.Shower(self.room))


    def prettier(self, dictio:dict=None):
        """ Pretty print all the keys and values of enterd
        dictionary for better reading and working  """
        if dictio:
            return pprint.pp(dictio, indent=4, dpeth=10)
        else:
            print("Pleas Enter A valid Dictionari :)")
        print('\n')
        self.leader_ship.setdefault("Familly", ("Lover", "Friends"))
        self.number = '09925741064'
        self.number = '60379353283'

# End