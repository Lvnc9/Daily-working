#!/usr/bin/python
# Start
# Module
from pathlib import Path
import glob
import os
import shutil


for filename in glob.glob("*.text"):
    print(filename)

lala = glob.glob('*.txt')
print(lala)



way = Path("sometexst.txt")

print(way.resolve())



class Identifier:
    """ Something """

    def __init__(self): 
        self.count = 1
        self.filenames = []
    def creater(self, name):
        """ creating a full path with the desirend name """
        self.filepath = Path(name).resolve()
        if not self.filepath.exists():
            with open(self.filepath, mode='wt') as file:
                pass
        
        self.filenames.append(self.filepath)
        
    def reader(self, name):
        for file in self.filenames:
            if name == file:
                readText = file.read_text()
                return readText

    
    def tree(self, pathdir):
        print(f"+ {pathdir}")
        for path in sorted(pathdir.rglob("*")):
            depth = len(path.relative_to(pathdir).parts)
            spacer = "      " * depth
            print(f"{spacer} + {path.name}")


# End