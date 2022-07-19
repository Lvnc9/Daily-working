#! python 3.9.2
# Start
# Chossing to when to choos a funcion and when to use an object
# Modules
import os

class Pashmak:
    "some none sence startation"

    def __init__(self, name:str, lname:str):
        "Declare two attrs"
        
        self._name = name
        self._lname = lname

    def _set_name(self, name):
        if not name:
            raise Exception("Can't accept empty string")
        self._name = name

    def _get_name(self):
        return self._name

    name = property(_get_name, _set_name, doc='IDK')
    lil_one = property

lil = Pashmak('Sam', 'mohammadi')
print(lil.name)
lil.name = "PashmakSS"
print(lil.name)
lil.name = 'bs'

class Silly:
    """A silly example that simply states whenever
    any of the methods are called"""

    def _get_silly(self):
        print("you are getting silly")
        return self._silly
    
    def _set_silly(self, value):
        print(f"You are making silly {value}")
        self._silly = value
    
    def _del_silly(self):
        print("Whoah, you killed silly")
        del self._silly
    
    silly = property(_get_silly, _set_silly,
    _del_silly, "This is a silly property")

test = Silly()
test.silly = "some value"
os.system('clear')
print(test.silly)


#class Foo:
#    @property
#    def foo(self):
#        return self._foo
#    
#    @foo.setter
#    def foo(self, value):
#        "Set an attribute for the property"
#        self._foo = value

class Silly:
    """Some silly object with silly working space :)"""
    @property
    def silly(self):
        """Silly property:
        a property that works on how silly you wanna see!
        IK that Sound awfull but here is the shot xD
        """

        print(f"Hey, this is a silly space!")
        return self._silly
    
    @silly.setter
    def silly(self, value):
        print(f"About to save {value}")
        self._silly = value
    
    @silly.deleter
    def silly(self):
        print(f"Oh noooo. you deleted silly :(")
        del self._silly



# End