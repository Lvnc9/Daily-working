#! python3
# Start
# A train file that helps the learner to look more deeper into the pashmaki house of Exceptions :)
# Modules
from collections.abc import Container
import random


some_exception = [ValueError, TypeError, IndexError, None]


try:
    choice = random.choice(some_exception)
    print(f'raising an Exception... {choice}')
    if choice:
        raise choice

except ValueError:
    print('Caught a ValueError')
except TypeError:
    print("Caught a TypeError")
except IndexError:
    print('Caught An Index Error')
except Exception as exc:
    print(f'Caught some other Error: {exc.__class__.__name__}')

else:
    print("this message Shell shown if no Exception Occures")

finally:
    print("this message shell always shown no mather what happens ")
     
# End