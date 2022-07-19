#! pyhton3.9.3
# Start
# Making the asked number of the directorys in the asked path 
# Modules
import sys
from pathlib import Path

# TODO:Taking the asked path for creating directorys
class Way(object):
    """ Gathering base information of the asked 
    directory for creating """

    def __init__(self, name:str, path:str):
        self.current = Path.cwd()
        self.name = name
        self.path = path
    
    @property.fget
    def name(self):
        return self.name
    
    @property.fset
    

# TODO:Name design


# TODO:Creating directorys 


# End