#! python3
# Start
# Modules
import os
import shutil
import send2trash
import zipfile


class Spliter:
    """Will split all the foolder and the
    sub foolders and files together and return
    it back"""
    
    def __init__(self, ready:str):
        "checking if the programmer is ready to walk"
        self.ready = ready.lower()
        
    def walker(self):
        if not self.ready.isalpha():
            print('you did not enter Letter')
            pass
            if self.ready == 'y' or self.ready[0] == 'y':
                for folderName, subfolders, filenames in os.walk('./Old_plus_1'):
                    print('The current folder is ' + folderName)

                    for subfolder in subfolders:
                        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

                    for filename in filenames:
                        print('FILE INSIDE ' + folderName + ': '+ filename)
                    print(''.center(50, '='),'\n')
            else:
                print('Have good day')

# Using some zip power :0

zip_obj = zipfile.ZipFile('./Daily/Days/Sat Jun 22/testlake.zip', 'w')

# Making a zip file
zip_obj = zipfile.ZipFile('./Daily/Days/Sat Jun 22/TestLake.zip', 'w')
zip_obj.write('./Daily/Days/pashmak.txt', zipfile.ZIP_DEFLATED)

# End