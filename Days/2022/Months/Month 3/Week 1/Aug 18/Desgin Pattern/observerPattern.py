#!/usr/bin/python
# Start
# Working on Observer Pattern
# Modules
from datetime import datetime
import itertools
import sys
import time


class Observed:

    def __init__(self):
        self.__observers = set()

    def observers_add(self, observer, *observers):
        # I like usingg itertools.chain(x, y) !
        for observer in itertools.chain((observer,), *observers):
            self.__observers.add(observer)
            observer.update(self)
    
    def observer_discard(self, observer):
        self.__observers.discard(observer)
    
    def observer_notify(self, observer):
        for observer in self.__observers:
            observer.update(self)


class SliderModel(Observed):

    def __init__(self, value, minimum, maximum):
        super().__init__()
        self.value = value
        self.minimum = minimum
        self.maximum = maximum 

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if self.__value != value:
            self.value = value
            self.observer_notify()

    @property
    def minimum(self):
        return self.__minimum
    
    @minimum.setter
    def minimum(self, min):
        if self.__minimum != min:
            self.__minimum = min
            self.observer_notify()

    @property
    def maximum(self):
        return self.__maximum

    @maximum.setter
    def maximum(self, max):
        if self.__max != max:
            self.__max = max
            self.observer_notify()


class HistoryView:
    
    def __init__(self):
        self.data = []

    # using stdout
    def update(self, model):
        self.data.append((model.value, time.time()))


class LiveView:

    def __init__(self, length=40):
        self.length = length

    # using stderr
    def update(self, model):
        tippingPoint = round(model.value * self.length /
                (model.maximum - model.minimum))
        td = '<td style="background-color: {}">&nbsp;</td>'
        html = ['<table style="font-family: monospace" border="0"><tr>']
        html.extend(td.format("darkblue") * tippingPoint)
        html.extend(td.format("cyan") * (self.length - tippingPoint))
        html.append("<td>{}</td></tr></table>".format(model.value))
        print("".join(html))

def main():
    historyView = HistoryView()
    liveView = LiveView()
    
    model = SliderModel(0, 0, 40) # minimum, value, maximum
    model.observers_add(historyView, liveView) # liveView produces output
    
    for value in (7, 23, 37):
        model.value = value             # liveView produces output
    for value, timestamp in historyView.data:
        print("{:3} {}".format(value, datetime.datetime.fromtimestamp(
            timestamp)), file=sys.stderr)

# End