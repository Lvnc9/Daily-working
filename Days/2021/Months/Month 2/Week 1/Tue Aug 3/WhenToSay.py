#! python3
# Start
# Deciding when to use decorators and this kind of bullshits xD
# Moduls
import os
# using some of property decorator
class Pashmak(object):
    """playing with the property funcion"""

    def _get_name(self):
        "get the name attr"
        print("you are about to see the pashmaks Color!")
        return self._pashmak

    def _set_name(self, name:str):
        print(f"you have set the name {name} attr")
        self._pashmak = name

    def _del_name(self):
        print("Whoah you delleted the attr :(")
        del self._pashmak
    
    pashmak = property(_get_name, _set_name, _del_name, """***API***
    Choos a color for the pashmak that you are about to buy""")

lil = Pashmak()
lil.pashmak = "Red"
print(lil.pashmak)


# Now it is the time to move forward and make the property funcion make the

class Lilone(object):
    """This lilone has got some pashamky new brand thing called
    decorators!!!"""

    @property
    def pashmak(self):
        print("Lil pashamks are always good as lil 2 are")
        return self._pashmaks_color
    @pashmak.setter
    def pashmak(self, pashmaks_color:str):
        """Will set an attribute"""
        
        pashmaks_color = str(pashmaks_color)
        if not pashmaks_color.isalnum():
            raise Exception("Oh no. you can only use letters an numbers!")
        self._pashmaks_color = str(pashmaks_color)
    
    @pashmak.deleter
    def pashmak(self):
        "Delete the pashmak attr"
        
        del self._pashmaks_color

os.system("clear")

lil2 = Lilone()
lil2.pashmak = 2
print(lil2.pashmak)
# End