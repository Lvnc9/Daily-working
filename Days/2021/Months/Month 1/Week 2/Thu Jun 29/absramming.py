#! python3 
# Start
# Modules (importing the base abstraction module :)
import abc
from collections.abc import Container

# Playing some abstracttion ;)
print(Container.__abstractmethods__)


class SillyContainer:
    def __contains__(self, x):
        if not isinstance(x, int) or not (x % 2):
            return False
        
        return True
class OddContainer:
    def __contains__(self, x):
        if not isinstance(x, int) or not x % 2:
            return False

        return True

lil = SillyContainer()
print(issubclass(SillyContainer, Container))

print(1 in lil)
print(2 in lil)
print(3 in lil)


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

# End