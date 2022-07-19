#! python3
# Start
# Backup all the files in the foolder and paste it into a zip file
# Whose its file name increase

# Modules 
import zipfile, os, sys

# Gather all the files
def backupToZip(folder:str, name:str):
    # Creating name for the zipfile
    "Back up the entire content of the current foolder"
    
    folder = os.path.abspath(folder)       # For Making sure the fooldername is absolute

    if not os.path.exists(folder):
        print(f"Sorry the {folder} doesn't exist!")
        sys.exit()
    # A counter that will increase and count the zip files number
    number = 1
    
    
    zipFileName = name  + '_' + str(number) + '.zip'
    number += 1
        
        
    # Making the zipfile 
    print(f'making the zipfile {zipFileName}'.title())
    zipbackup = zipfile.ZipFile(zipFileName, 'w')


    # walk in entire foolder and back up all the files in the foolder
    for foldername, subfoolders, filenames in os.walk(folder):
        print(f'Adding the foolder to the {foldername}')
        # Add the current folder to the ZIP file.
        zipbackup.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            # don't backup the backup ZIP files
            zipbackup.write(os.path.join(foldername, filename))

    zipbackup.close()
    print('Finished!')


#backupToZip('./Old_plus_2/Project`')
backupToZip('./Old_plus_2/Project', 'lilone')
# End