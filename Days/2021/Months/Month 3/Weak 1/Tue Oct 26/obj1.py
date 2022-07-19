#! python3.9.2
# Start
# When to use objects and when to use not them
# TODO: Modules

class Polygon:
    def __init__(self):
        self.calculater = percalcu()

def percalcu(n:int=0):
    if not n:
        print(f""" Default Value of the percalculater!
        if n = 0 : n**2 - 1 = {n**2 - 1} """)


class Color:
    """ Working with the property and """
        
    def __init__(self, rgb_name:str, number:int):
        self._rgb_name = rgb_name
        self._number = number

    def _set_number(self, number):
        if number % 2:
            raise Exception("Number Is Even")
        
        self._number = number

    def _get_number(self):
        return self._number

    name = property(_get_number, _set_number)

lilTest = Color('Moly', '2')
print(lilTest.name)

# End