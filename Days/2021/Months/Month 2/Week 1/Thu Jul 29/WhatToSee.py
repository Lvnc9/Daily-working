#! python 3.9.2
# Start
# when to ues objects and not functions
# Modules

def pashmak(n):
    return n

class Pashmak:
    "return the entered value"
    def __init__(self, n:int):
        self.n = n
    
    def returning(self):
        return self.n

lil = Pashmak(2)
lil.returning()


# End