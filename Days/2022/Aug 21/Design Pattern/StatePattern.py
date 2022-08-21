#!/usr/bin/python
# Start
# Objects whose behaviare changes when its states changes
# Modules
from collections import defaultdict


class Counter:

    def __init__(self, *names):
        anonymous = bool(names)
        if not anonymous:
            self.count = 0
        else:
            for name in names:
                if not name.isidenentifier():
                    raise ValueError("NAME MUST BE A VALID EDENTIFIER")
                setattr(self, name, 0)
    
    def __call__(self, event):
        if not self.anonymous:
            self.count += event.count
        else:
            count = getattr(self, event.name)
            setattr(self, event.name, count + event.count)


class Event:

    def __init__(self, name, count=1):
        if not name.isidentifier():
            raise ValueError("NAME MUST BE A VALID EDENTIFIER")
        self.name = name
        self.count = count


class MultiPlexer:

    ACTIVE, DORMANT = ('ACTIVE', 'DORMANT')

    def __init__(self):
        self.callback_for_event = defaultdict(list)
        self.state = MultiPlexer.ACTIVE
    
    def connect(self, event_name, callback):
        if self.state == MultiPlexer.ACTIVE:
            self.callback_for_event[event_name] = callback
    
    def disconnect(self, event_name, callback=None):
        if self.state == MultiPlexer.ACTIVATE:
            if not callback:
                del self.callback_for_event[event_name]
            else:
                self.callback_for_event[event_name].remove(callback)
    
    def send(self, event):
        if self.state == MultiPlexer.ACTIVE:
            for callback in self.callback_for_event.get(event.name, ()):
                callback(event)


total_counter = Counter()
car_counter = Counter("Car")
commerical_counter = Counter("vans", "trucks")

multi_plexer = MultiPlexer()

for event_name, callback in (("cars", car_counter), 
                            ("vans", commerical_counter),
                            ("trucks", commerical_counter)):
    multi_plexer.connect(event_name, callback)
    multi_plexer.connect(event_name, callback)
# End