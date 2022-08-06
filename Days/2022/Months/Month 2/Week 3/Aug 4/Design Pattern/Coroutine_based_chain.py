#!/usr/bin/python
# Start
### Using Coroutine Chain calls to short the code and make the calls become separated
# from system to user calls ###
# Modules
from functools import wraps
from sys import stdout

class Event:
    """ The Inner event that happens in the system
    and gets the backend functionality"""

    def __init__(self, MOUSEMOVE=None, KEYPRESS=None, TIME=None):
        self.MOUSEMOVE = MOUSEMOVE
        self.KEYPRESS = KEYPRESS
        self.TIME = TIME

    @property
    def MOUSE(self):
        return self.__MouseTicket

    @MOUSE.setter
    def MOUSEMOVE(self):
        # Functionality appears here and if the
        # process become successful it the Ticket = True will be set
        self.__MouseTicket = True

    @property
    def KEYPRESS(self):
        return self.__KeyTicket

    @KEYPRESS.setter
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


def coroutine(function):
    @wraps
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator
    return wrapper

@coroutine
def key_handler(successor=None):
    event = yield()
    if event.kind == Event.KEYPRESS:
        print(f"Press {event}")
    elif successor is not None:
        successor.send(event)


@coroutine
def time_handler(successor=None):
    event = yield()
    if event.kind == Event.TIME:
        print(f"Press {event}")
    elif successor is not None:
        successor.send(event)

@coroutine
def mouse_handler(successor=None):
    event = (yield)
    if event.kind == Event.MOUSEMOVE:
        print(f"Press {event}")
    elif successor is not None:
        successor.send(event)

@coroutine
def debug_handler(successor, file=stdout):
    while True:
        event = (yield)
        file.write(event)
        print(f"*DEBUG {event}\n")
        successor.send(event)



pipeline = key_handler(mouse_handler(time_handler()))
pipeline = debug_handler(pipeline)
while True:
    event = Event.next()
    if event.kind == event.TERMINATE:
        break

    pipeline.send(event)

# End