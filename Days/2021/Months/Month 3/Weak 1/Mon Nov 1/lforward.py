#! python3.9.2
# Start
# learning the chapter 5 of the OOP book. learning the techniques that can be used when using objects
# TODO: Modules


class LilTest(object):
    """ Testing the method-based syntax """

    def __init__(self, name:str, fname:str):
        self._name = name
        self._fname = fname

    def _set_name(self, name):
        if not name:
            raise Exception("Enter a valid name")
        
        self._name = name
    
    def _get_name(self):
        return self._name
    
    name = property(_get_name, _set_name)


lil = LilTest("Abouter", "OF the world S)")
lil.name = "Someone you knew before :("
print(lil.name)

class UltimatedLil(object):
    def __init__(self, name:str='', **kwargs):
        super().__init__(**kwargs)
    
        self.name = name
    
    @property.fget
    def foo(self):
        return 2
    
# End