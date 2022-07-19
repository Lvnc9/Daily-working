#! python3
# Start
# Modules
import traceback
import logging
import os 



os.system('clear')
npashmak = 21

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s == %(levelname)s == %(message)s')

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s') 
logging.debug('Start the program')


def factorial(n):
    logging.debug(f'Start of factorial {n}')
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug(f'End of factorial {n}')
    return total

print(factorial(5))
logging.debug('End of program')

# End