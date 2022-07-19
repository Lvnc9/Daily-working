#! python3.9.8
# Start
# Well IDK yet but i have to look back to some old stuff of my school and back to my time you know :)
# TODO: Modules
class AnTest(object):
    """ Shows the power of property keyword funcion """
    def __shower(self):
        """ Making A new property who maks an good name """
        print("\nShowing the variable:")
        return self._name

    def __stter(self, name:str):
        print("Ok We have to set a new name")
        self._name = name
    
    def __deleter(self):
        print("Are you sure of deleting the current name? Y/N")
        ans = str(input())
        if 'y' or 'Y' in ans:
            del self._name
            print("NAME SUCCECFULLY DELETED")
        print("NAME DIDN'T CHANGE")

    name = property(__shower, __stter, __deleter)

    def __str__(self):
        return self.name

sos = AnTest()
sos.name = 'idk'
print(sos)
# End