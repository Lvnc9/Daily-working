#! python3.9.2
# Start
# training the old tought of Chapter(5, 3)

""" Not decided yet to what the fuck gonna happend in this python file
but propobly it gets to the time i go and write the new program or the project
 """

# TODO: Modules

# Testing the abilitys

""" this will make a long set of data """
test = (1, 2, 3, 4,)
test2 = (5, 6, 7, 8)

def pashmak():
    print("IDK somehow i am gettign to be existed for now )s")

# and now then go to thgo the class

class Color:
    """ Learning the usage of the property keyword """

    def __init__(self, rgb_value, name):
        self._rgb_value = rgb_value
        self._name = name
    
    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        
        self._name = name
    
    def _get_name(self):
        return self._name
    
    name = property(_get_name, _set_name)

lil = Color("#0042rw", 'lil-sam')

lil.name = '3'
print(lil.name)

class Silly:
    """ Making some Silly pashmaky proprty who talks
    about fget fset and fdel and doc """

    def _get_silly(self):
        print("You're Watching Silly")
        return self._silly 
    
    def _set_silly(self, silly:str):
        print(f"you've set silly {silly}")
        self._silly = silly

    def _del_silly(self):
        ques = str(input("Are you sure for deleting the silly property?(y/n\n"))
        
        while not 'y' or 'n' in ques:
            ques = str(input("Are you sure for deleting the silly property?(y/n\n"))

        if ques == 'y':
            print("Ohh noooo,\nYou have killed Silly!")
            
            del self._silly
        
    silly = property(_get_silly, _set_silly, _del_silly, "This is a sily proprty")

lil = Silly()
lil.silly = 'Embareced'

print(lil)
help(Silly)
# End