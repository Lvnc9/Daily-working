#!python3.9.9
# Start
# using Data structures and usage of them
# Modules
from collections import namedtuple
from collections import defaultdict
class HolderObject(object):
    """ Working on data structores including tuples & 
    dictionaries & list and ... """
    Familly = namedtuple("familly", "Leon Asuka Shinji Katsuragi PenPen")
    
    def __init__(self, familly:Familly, places:dict):
       self.familly = familly
       self.places = places


lil_test = HolderObject(('True True True True'), {})
print(lil_test.familly)

def letter_frequency(sentence:str):
    frequencies = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1
        print(frequency)
    return frequencies

def letter_frequency2(sentence:str):
    """ count how many times a letter repeates
    in a sentence """
    frequency = defaultdict(int)
    for letter in sentence:
        frequency[letter] += 1
    
    return frequency

#print(letter_frequency("somehow"))
print(letter_frequency2('hello man how are you doing bro ofcourse my bro i shall do that'))

# End