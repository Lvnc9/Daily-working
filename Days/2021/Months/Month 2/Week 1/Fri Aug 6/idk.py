#! python3.9.2
# Start
# Learning the new path lib xD
# Modules
import glob
import shutil
import os

# Using new pathlib lil pashmak :|
for filename in glob.glob("*.text"):
    new_path = os.path.join("archive", filename)
    shutil.move(filename, new_path)



# End