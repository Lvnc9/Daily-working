#! python3.9.9
# Start
# Using string Modules and working with lists
# Module
import string

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

#End
