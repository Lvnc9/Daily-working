#! python 3.9.2
# Start
# Some random numbers xD
# Modules
import shutil
import os
import zipfile
import sys
from pathlib import Path

# How to follow the DRY princible
class ZipProcessor:
    """Minimize the DRY princible for better
    undertstanding"""

    def __init__(self, zip_name:str):
        self.zip_name = zip_name
        self.temp_directory = Path(f"Unzipped-{zip_name[:-1]}")
    
    def process_zip(self):
        self.unzip_files()
        self.process_files()
        self.zip_file()

    def unzip_files(self):
        "Unzip all the file of Zipfile in a temp_directory"

        with zipfile.ZipFile(self.zip_name) as zip:
            zip.extractall(str(self.temp_directory))

    def zip_file(self):
        """Zip all the changed files of the
        temp_direcotry in a new zipfile"""

        with zipfile.ZipFile(self.zip_name) as file:
            for file_name in  self.temp_directory.iterdir:
                file.write(str(file_name), file_name.name)

            shutil.rmtree(str(self.temp_directory))


# And the Old ZipReplace :)
class ZipReplace(ZipProcessor):
    """Will replace the content of files of the 
    specified zipfile"""

    def __init__(self, filename:str, search_string:str, replace_string:str):
        super().__init__(filename)
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self):
        """ Perform a find and replace on all files in 
        the temp Directory """

        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
                contents = contents.replace(self.search_string,
                self.replace_string)
            
            with filename.open('w') as file:
                file.write(contents)

if __name__ == "__main__":
    ZipReplace(*sys.argv[1:4]).process_zip()


# End