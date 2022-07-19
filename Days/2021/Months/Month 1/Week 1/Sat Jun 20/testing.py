#! python3
# Start
# Modules
import os
import shutil
import send2trash

for folderName, subfolders, filenames in os.walk('./Old_plus_1'):
    print('The current folder is ' + folderName)
    
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
    print(''.center(50, '='),'\n')


for foldername, subfolders, filename in os.walk('./Old_plus_2'):
    print('\n', ''.center(50, '='))
    print('The Current foldername is: ', foldername)

    for subfoolder in subfolders:
        print('The Current subfolder name is:', subfoolder)

    for filename in filenames:
        print('The Current filename is: ', filename)

# End