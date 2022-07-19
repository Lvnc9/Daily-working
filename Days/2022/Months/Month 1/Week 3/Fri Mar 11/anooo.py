#! python3.9.9 
# Start
# Modules
from collections import namedtuple, defaultdict, Counter
from functools import total_ordering
from queue import Queue, LifoQueue

# The Main Core of the tree object
pashmaktest = {'the data'}

test_object = Queue(maxsize=3)
test_object.put((1, 'two'))
test_object.put((2, 'three'))
test_object.put((3, 'four'))

while test_object:
    print(test_object.get())


# End