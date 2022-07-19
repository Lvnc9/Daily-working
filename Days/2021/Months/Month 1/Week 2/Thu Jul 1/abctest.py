#! python
# Start
# This pashmaky file created to show the pashmak powers of the abstaction and duck typing :)))
# Modules
import  abc
from collections.abc import Container



# Crating a pashmak istance of the Container abc obj
class Pashmak:
    def __contains__(self, x):
        if not isinstance(x, int) or not (x % 2):
            return False
        
        return True

lil = Pashmak()

class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractproperty
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented



class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractproperty
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        
        return NotImplemented
    
    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethod__) <= attrs:
                return True
        
        return NotImplemented

    @
# End