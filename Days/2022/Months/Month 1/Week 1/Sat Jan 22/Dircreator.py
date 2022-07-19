#! python3.9.9
# Start
# Modules
from pathlib import Path
import os
os.chdir('/home/fvolizer/{ my movis:) }/Bleach')
current = '/home/fvolizer/{ my movis:) }/Bleach/100'
number = 0
while not number == 100:
    os.mkdir(Path.cwd().joinpath(str(number)))
    number += 1
# End