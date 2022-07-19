#! python3
# Start
# Pashmaki test for writing some pashmaki new code from the OOP code ;)
# Modules
from collections.abc import Container


class Test:
    'A test class that instances from the abstraction class'

    def __contains__(self, x):
        if not isinstance(int, x) or x % 2:
            return False

        return True
print(Container.__abstractmethods__)


class EvenNumber(list):
    "Take only Even numbers else return Error"

    def append(self, integer):
        """Determines the even number
        add the number to the list if its even """
        if not isinstance(integer, int):
            raise TypeError('Only Acceptes Integers!!!')
        elif integer % 2:
            raise ValueError('Only Takes Even numbers!!!')
            
        super().append(integer)


class FunnyDivision():
    "Divide 100 to the enetered number and mock :)"

    def divider(self, number):
        try:
            if number == 13:
                raise ValueError('Nah thats a unlucky number Dude ')
            return 100 / number
        except (ZeroDivisionError, TypeError):
            return "WTF?\ninvalid Number!"

#lil = FunnyDivision()
#for val in (0, 13, 'hello'):
#    print(f'Testing Value {val}', end=' ')
#    print(lil.divider(val))


def funny_division3(anumber):
    try:
        if anumber == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / anumber
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print("No, No, not 13!")
        raise

funny_division3(0)
# And some of the pashamks do not allow to come to the pashmak house i guess
try:
    100 / 0
except Exception as el:
    print('the Exceptions Argumant were', el.with_traceback)

# End