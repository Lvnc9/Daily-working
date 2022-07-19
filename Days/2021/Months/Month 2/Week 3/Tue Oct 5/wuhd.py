#! python3.9.2
# Start
# TODO: Explaining the porpuse of the code file
# Modules
from collections import namedtuple, defaultdict
import pprint
pashmak = namedtuple('pashmak', 'Currency Top Low Middle')
pashmak = pashmak(42, 59, 29, 44)

print(type(pashmak))

sentence = "Hello, World!, this is another version of saying bullshit"

def letter_frequency(sentence):
    "Count the number of times letters occure"

    frequencies = {}

    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)


def nv_letter_frequency(sentence):
    "Counting the number of times a letter occured"

    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1

    print(type(frequencies))    
    return pprint.pprint(frequencies)

print(nv_letter_frequency(sentence))


# End