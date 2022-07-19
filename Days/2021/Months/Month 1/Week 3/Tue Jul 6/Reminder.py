#! python3
# Start
# This File is a Reminder of the elements that we had learn in the past days 
# Modules
from collections.abc import Container
import abc

class OddFinder(object):
    "A duck type abstraction Instance!"

    def __contains__(self, integer):
        try:
            if not isinstance(integer, int):
                raise TypeError('Only Integers Allowed')
            if integer % 2:
                return True
            return False
        except Exception as exc:
            print('Exception accured', exc.args)

lil = OddFinder()
print(lil.__contains__('hello'))

print(2 in lil, 3 in lil, 4 in lil)


# End