#! python 3.9.2
# Start
# testing some abstraction pashamky things
# Modules
import abc

class MediaLoader(metaclass=abc.ABCMeta):
    """To ducument what API the third party
    plugins should provide"""

    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractproperty
    def exit(self):
        pass


class EvenNumber(Exception):
    """Error. if the number is not even it shell raise an error"""

    def __init__(self, number:int):
        super().__init__(f"Unfortunetly\n The number {number} is not an Even number")
    
    
raise EvenNumber(2)

# End