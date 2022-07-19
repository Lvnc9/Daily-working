#! python3.9.2
# Start 
# How to work with the singletonobject law xD
# Modules
import logging

# Singleton object that can get only an one instance
class SingletonObject(object):
    """ Prototype the Singletonobject to show how it can
    works """

    class __SingletonObject:
        def __init__(self):
            self.file_name = None

        def __str__(self):
            return "{0!r} {1}".format(self, self.file_name)
    
    instance = None

    def __new__(cls):
        if not SingletonObject.instance:
            SingletonObject.instance = SingletonObject.__SingletonObject()
        
        return SingletonObject.instance
    
    def __getattr__(self, name):
        return getattr(self.instance, name)
    
    def __setattr__(self, name):
        return setattr(self.instance, name)
        
lil = SingletonObject()
lil.file_name = 2
print(lil)
a = SingletonObject()
a.file_name = 3
print(a)


class SingletonObject(object):
    """ Prototype the Singlton class design
    show how it works when applying it """

    class __SingletonObject:
        def __init__(self):
            self.file_name = None
        
        def __str__(self):
            return "{0!r} {1}".format(self, self.file_name)

    instance = None

    def __new__(cls):
        if not SingletonObject.instance:
            SingletonObject.instance = SingletonObject.__SingletonObject()
    
        return SingletonObject.instance
    
    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)
# End