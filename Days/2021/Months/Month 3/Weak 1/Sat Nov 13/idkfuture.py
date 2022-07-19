#! python3.9.2
# Start
# rewriting the old codes of a text replacer of all the text files of a zip file
# Modules
import shutil 
import sys
import zipfile
from pathlib import Path

# TODO: The base System of replacing the desired texts with the replaced one
class ZipReplacer(object):
    """ gets the base parameters to find the wanted zipfile
    whoa has text files in it. Changing the texts we are loocking
    for and replacing them with the texts we ordered """

    # Initializing the needed attributes
    def __init__(self, file_name:str, search_string:str, replace_string:str):
        self.file_name = file_name
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = Path(f"unzipped-{self.file_name}")

    # TODO: Object manager for connecting methods together
    def unzip_replace_zip(self):
        pass

    # Extracter zipfile
    def unzipper(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.file_name) as zip:
            zip.extractall(str(self.temp_directory))            

    # Replacing txts
    def find_replace(self):
        for filename in self.temp_directory.iterdir():
            with filename.open as file:
                contents = file.read()
            
            contents = contents.replace(
                self.search_string, self.replace_string)

            with filename.open('w') as file:
                file.write(contents)
    
    # ziping all the files together 
    def zip_files(self):
        with zipfile.ZipFile(self.file_name, 'w') as zip:
            for file in self.temp_directory.iterdir():
                zip.write(str(file), file.name)
        
        shutil.rmtree(str(self.temp_directory))

if __name__ == "__main__":
    ZipReplacer(*sys.argv[1:4]).unzip_replace_zip()
# End