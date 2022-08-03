#!/usr/bin/python
# Start
# Gets some events from the user and some of them from the system
# and tries to fallow the Chain Responsibility behavioral pattern ###

from pyrsistent import T
from requests import NullHandler


class Event:
    """ The Inner event that happens in the system
    and gets the backend functionality"""

    def __init__(self, MOUSE=None, KEY=None, TIME=None):
        self.MOUSE = MOUSE
        self.KEY = KEY
        self.TIME = TIME

    @property
    def MOUSE(self):
        return self.__MouseTicket

    @MOUSE.setter
    def MOUSE(self):
        # Functionality appears here and if the
        # process become successful it the Ticket = True will be set
        self.__MouseTicket = True

    @property
    def KEY(self):
        return self.__KeyTicket

    @KEY.setter
    def KEY(self):
        # Functionality appears here and if the
        # process become successful it the Ticket = True will be set
        self.__TimeTicket = True

    @property
    def Time(self):
        return self.__KeyTicket

    @Time.setter
    def Time(self):
        # Functionality appears here and if the
        # process become successful it the Ticket = True will be set
        self.__TimeTicket = True

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

class KeyHandler(NullHandeler):

    def handle(self, event):
        if event.kind == EVENT.Key:
            print(f"Click: {event}")
        else:
            super().__handle(event)

class TimerHandler(NullHandeler):

    def handle(self, event):
        if event.kind == EVENT.Time:
            print(f"Click: {event}")
        else:
            super().__handle(event)

class DebugHandler(NullHandler):
    def __init__(self, successor=None, file=sys.stdout):
        super().__init__(successor)

    def handle(self, event):
        self.__file.write(f"*DEBUG* : {event}\n")
        super().handle(event)


EVENT = Event()
handler1 = TimerHandler(KeyHandler(MouseHandler(NullHandler())))
handler2 = DebugHandler(handler1)

# End