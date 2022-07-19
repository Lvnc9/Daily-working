#! python3
# Start
# A test programm that works with the coin and then debug it!
# Modules
import random
import logging
import os

os.system('clear')
heads = 0

for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads += 1

    if i == 500:
        print('Halfway done!')
print('Heads came up ' + str(heads) + ' times.')

logging.basicConfig(level=logging.DEBUG, foramt=' [%(levelname)s]- - -%(asctime)s- - -%(message)s')

logging.warning('The program did not complete Right!')

# End