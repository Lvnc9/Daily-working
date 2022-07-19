#! python3.9.2
# Start
# Loocking back to the old thought infofrmatioans of the chapter 5 of oop book
# Modules

class SomeWhat(object):
    """ some useless object who showd the property
    funcion and decorator """

    def _lil(self):
        pass

    def _not_lil(self): 
        pass

    lil = property(_not_lil, _lil)

    @property
    def idk(self):
        pass

idk = SomeWhat()

# End