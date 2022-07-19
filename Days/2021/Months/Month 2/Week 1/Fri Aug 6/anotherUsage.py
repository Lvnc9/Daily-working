#! python 3.9.2
# Start
# Again some lil cosmized attrs
# Modules
import sys
import shutil
import zipfile
from pathlib import Path


# How the Gfunction can work
class AverageList(list):
    """Get an average of the given list and return
    it back
    
    using property get atter"""

    @property
    def average(self):
        return sum(self) / len(self)

# Actual code
class ZipReplace:
    """Represent A zipfile. Having it to give it
    to the manage object to control the pashmaks"""

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
        self.temp_directory().mkdir()
        with zipfile.ZipFile(self.filename) as zip:
            zip.extractall(str(self.temp_directory))


    def find_replace(self):
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            
            contents = contents.replace(self.search_string, self.replace_string)

            with filename.open("w") as file:
                file.write(contents)
    
    def zip_file(self):
        with zipfile.ZipFile(self.filename) as zip:
            for filename in self.temp_directory.iterdir():
                zip.write(str(filename), filename.name)
        
        shutil.rmtree(str(self.temp_directory))


if __name__ == "__main__":
    ZipReplace(*sys.argv[1:4]).zip_find_replace


# End