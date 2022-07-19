#! python3.9.2
# Start
# Talk about the power of dictionari
# TODO Modules
from collections import namedtuple

Lake_family = {
    "Left Side" : ("Canons", "Harlys", "Thoms"),
    "Right Side" : ("rooli", "holy", "maks")
}

class TestObject(object):
    """ Test object for proving the usage of 
    objects as keys in dictionari """
    
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'TestObject'
my_obj = TestObject(12)

Lake_family[my_obj] = "Storing an object as a key"
print(Lake_family)
print(TestObject)
# End