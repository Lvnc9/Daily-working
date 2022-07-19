#! python3.9.9
# Start
# End of Chapter 6 of OOP is near talking about the last Areal of it
# Modules
from queue import Queue
from queue import LifoQueue
from functools import total_ordering
import time

# Working with FifoQueue as it is a real Queue
some_fifoQueue = Queue(6)
some_fifoQueue.put('h')
some_fifoQueue.put('e')
some_fifoQueue.put('l')
some_fifoQueue.put('l', block=False, timeout=2.5)
some_fifoQueue.put('o')

# Working with LifoQueue as it is like a rael Stack
some_lifoQueue = LifoQueue(maxsize=14)

# TODO:DONE Testing the possiblitty of checking the length of an Existening data structure


# Testing showing the Queue Data structures for the growing powert :)
print('o')
while not some_fifoQueue.empty():
    new_var = some_fifoQueue.get()
    print(new_var, end='')
    time.sleep(1)


# End