#! python3.9.2
# Start
# Object manager for lil objects
# Making the code readiablity and partinioning and extensibility 
# Modules
from pathlib import Path
import sys
import shutil
import zipfile
import os
 
class ZipReplace:
    """ Making a protype of the Obejct manager concept """

    def __init__(self, filename:str, search_string:str, replace_string:str):
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = Path(f"Unzipped-{filename}")

    def zip_find_replace(self):
        self.unzip_files()
        self.find_replace()
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.filename) as zip:
            zip.extractall(str(self.temp_directory))
    
    def find_replace(self):
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(self.search_string,
            self.replace_string)

            with filename.open(mode='w') as file:
                file.write(contents)
            
    def zip_files(self):
        with zipfile.ZipFile(self.filename, "w") as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)

if __name__ == "__main__": 
    ZipReplace(*sys.argv[1:4]).zip_find_replace() 
# End