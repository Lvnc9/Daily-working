#! python3.9.2
# Start
# Creating an Object that can manage the other objects
# Modules
from pathlib import Path

class ZipReplace:
    """Document the object manager pashmaky teory
    using a sngle method that represent the other methods
    to use the  three
    *Readability
    *Extensibility
    *Partitionning"""

    def __init__(self, filename:str, search_string:str, replace_string:str):
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = Path(f"unzipped-{filename}")


    @property
    def foo(self):
        return f"Now you are watching {self._foo}"
    
    @foo.setter
    def foo(self, message:str):
        print("you are about to save a attribute name foo")
        self._foo = message
    
    @foo.deleter
    def foo(self):
        print("whoah you deleted the pashmaki foo :}")
        del self._foo

lil_pashmak = ZipReplace("name", "holy", "Expierd")
lil_pashmak.foo = "IDK"
print(lil_pashmak.foo) 
# End