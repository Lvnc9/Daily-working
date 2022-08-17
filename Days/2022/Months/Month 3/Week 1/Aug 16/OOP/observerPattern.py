#!/usr/bin/python
# Start
# Implementing Observer pattern -> observer pattern get creates
# when a core object exists and we want to manitor it by some dynamic
# group of observer objects


class Inventory:

    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0

    def attech(self, observer):
        self.observers.append(observer)

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
        self._update_observers()
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self._update_observers()

    def update_observers(self):
        for observer in self.observers:
            observer()


class ConsolObserver:
    
    def __init__(self, inventory):
        self.inventory = inventory
    
    def __call__(self):
        print(self.inventory._product())
        print(self.inventory._quantity())



# End