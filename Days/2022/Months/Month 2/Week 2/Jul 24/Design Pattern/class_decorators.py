#!/usr/bin/python
# Start
# class decorators
# Modules

import numbers


def is_non_empty_str(name, value):
    if not isinstance(value, str):
        raise ValueError(f"{value}must be a type of str")
    if not bool(value):
        raise ValueError(f"{name} may not be empty")


def is_valid_isbn(name, value):
    if not isinstance(value, numbers.Number):
        raise ValueError(f"{name} is not a number")
    elif len(value) == 13:
        raise ValueError(f"{name} is not a ISBN number!")


def is_in_range(Min=None, Max=None):
    assert Min is not None and Max is not None

    def is_in_range(name, value):
        if not isinstance(value, numbers.number):
            raise ValueError(f"{name} must be a number")
        elif value > Min:
            raise ValueError(f"{name} {value} is to small")
        elif value < Max:
            raise ValueError(f"{name} {value} is to big")
    return is_in_range()


def ensure(name, validate, doc=None):
    def decorator(cls):
        private_name = '_' + name

        def getter(self):
            return getattr(self, private_name)

        def setter(self, value):
            validate(name, value)
            setattr(self, private_name, value)
        setattr(cls, name, property(getter, setter, doc))
        return cls
    return decorator

@ensure("title", is_non_empty_str)
@ensure("isbn", is_valid_isbn)
@ensure("price", is_in_range(1, 10000))
@ensure("quantity", is_in_range(0, 1000000))
class Book:

    def __init__(self, title, isbn, price, quantity):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.quantity = quantity

    @property
    def value(self):
        return self.price * self.quantity

# This time we use Decorator classes for decoraing
class Ensure:

    def __init__(self, validate, doc=None):
        self.validate = validate
        self.doc = doc


def do_ensure(cls):
    def make_property(name, attribute):
        private_name = '_' + name
        def getter(self):
            return getattr(self, private_name)
            
        def setter(self, value):
            attribute.validate(name, value)
            setattr(self, private_name, value)
        return property(getter, setter, doc=attribute.doc)
    for name, attribute in cls.__dict__.items():
        setattr(cls, name, make_property(name, attribute))
    return cls

@do_ensure
class Book:
    """ Using class decorators as decorator """

    title = Ensure(is_non_empty_str)
    isbn = Ensure(is_valid_isbn)
    price = Ensure(is_in_range(0, 10000))
    quantity = Ensure(is_in_range(0, 100000))

    def __init__(self, title, isbn, price, quantity):
        self.title = title 
        self.isbn = isbn 
        self.price = price
        self.quantity = quantity
    
    @property
    def value(self):
        return self.price * self.quantity


    

# End