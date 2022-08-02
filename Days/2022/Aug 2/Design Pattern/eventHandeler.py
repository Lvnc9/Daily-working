#!/usr/bin/python
# Start
### Gets some events from the user and some of them from the system
# and tries to fallow the Chain Responsibility behavioral pattern ###

class NullHandeler:
    """ the base class of the chain calls """

    def __init__(self, successor=None):
        self.__successor = successor
    
    def handle(self, event):
        if self.__successor is not None:
            self.__successor.handle(event)
    

class MouseHandler(NullHandeler):
    
    def handle(self, event):
        if event.kind == EVENT.MOUSE:
            print(f"Click: {event}")
        else:
            super().__handle(event)


# End