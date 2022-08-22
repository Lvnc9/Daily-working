#!/usr/bin/python
# Start
# Objects whose behaviare changes when its states changes 
# As Same as StatePattern1 but in in this time uses state-speciﬁc
# methods rather than the state-sensitive
# methods shown in the previous app
# Moudles
import collections


class Counter:

    def __init__(self, *names):
        self.anonymous = not bool(names)
        if self.anonymous:
            self.count = 0
        else:
            for name in names:
                if not name.isidentifier():
                    raise ValueError("names must be valid identifiers")
                setattr(self, name, 0)


    def __call__(self, event):
        if self.anonymous:
            self.count += event.count
        else:
            count = getattr(self, event.name)
            setattr(self, event.name, count + event.count)


class Event:

    def __init__(self, name, count=1):
        if not name.isidentifier():
            raise ValueError("names must be valid identifiers")
        self.name = name
        self.count = count


class Multiplexer:

    ACTIVE, DORMANT = ("ACTIVE", "DORMANT")

    def __init__(self):
        self.callbacksForEvent = collections.defaultdict(list)
        self.state = Multiplexer.ACTIVE


    @property
    def state(self):
        return (Multiplexer.ACTIVE if self.send == self.__active_send
                else Multiplexer.DORMANT)


    @state.setter
    def state(self, state):
        if state == Multiplexer.ACTIVE:
            self.connect = self.__active_connect
            self.disconnect = self.__active_disconnect
            self.send = self.__active_send
        else:
            self.connect = lambda *args: None
            self.disconnect = lambda *args: None
            self.send = lambda *args: None


    def __active_connect(self, eventName, callback):
        self.callbacksForEvent[eventName].append(callback)


    def __active_disconnect(self, eventName, callback=None):
        if callback is None:
            del self.callbacksForEvent[eventName]
        else:
            self.callbacksForEvent[eventName].remove(callback)


    def __active_send(self, event):
        for callback in self.callbacksForEvent.get(event.name, ()):
            callback(event)


total_counter = Counter()
car_counter = Counter("Car")
commerical_counter = Counter("vans", "trucks")

multi_plexer = Multiplexer()

for event_name, callback in (("cars", car_counter), 
                            ("vans", commerical_counter),
                            ("trucks", commerical_counter)):
    multi_plexer.connect(event_name, callback)
    multi_plexer.connect(event_name, callback)

# End