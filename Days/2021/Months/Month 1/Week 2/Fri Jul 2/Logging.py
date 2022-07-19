#! python3
# Start
# Modules
import logging
import traceback
logging.disable()
number_pashmak = 211
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s --- %(levelname)s --- %(message)s')

def factorial(n):
    """Get a single argumant and multiply it as a factorial
    for Example for n : N!: n * (n-1) (n-2) * ..."""
    
    logging.debug(f'Programm starts with the number {str(n)}')
    if n > 1:
        return n * (factorial(n - 1))
        logging.debug(f'Current number of {str(n)}')    
    return n
    logging.debug('programm has Successfully finished'.title())

print(factorial(5))
logging.debug('Some debugging info')
logging.info('{} is working fine')
logging.warning('{} is not working  as  expected. about to give a error log')
logging.error('{} caused error and not working')
logging.critical('Program about to crash in line  of {}')


print('Enter the first number to add:')
first = input()
print('Enter the second number to add:')
second = input()
print('Enter the third number to add:')
third = input()
print('The sum is ' + first + second + third)



# End