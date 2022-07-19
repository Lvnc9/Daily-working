#!python3.9.9
# Start
# using Data structures and usage of them
# Modules
from collections import namedtuple
from collections import defaultdict
from collections import Counter
import string

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


num_items = 0

def tuple_counter():
    global num_items 
    num_items += 1
    return(num_items, [])

some_d = defaultdict(tuple_counter)
some_d['a'][1].append(('lo lo', 'ho ho', 'ba Hahaha Hahahahaha Ha'))

print(some_d)

# The Shortest way to count number of times that a letter gets repeated

def counter_2(sentence:str):
    return Counter(sentence)


responses = [
    "vanilla",
    "chocolate",
    "vanilla",
    "vanilla",
    "caramel",
    "strawberry",
    "vanilla"
]
print(f"The Children Voted for {Counter(responses).most_common(1)} Ice cream")

testing1 = [1, 2, 3, 4, 5] + [' ']

CHARACTERS = list(string.ascii_letters) + [' ']

def frequency_letters(sentence:str):
    """ Count the number of the times that
    a valid character that is avalable in the ascii_letters
    is showed up  """

    frequencies = [(c, 0) for c in CHARACTERS]
    for letter in sentence:
        index = CHARACTERS.index(letter)
        frequencies[index] = (letter, frequencies[index][1]+1)
    
    return frequencies


print(frequency_letters("For Example of a man who did not wanted to end his life but he had not choice"))
# End