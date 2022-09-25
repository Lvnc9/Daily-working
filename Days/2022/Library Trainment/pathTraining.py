#!/usr/bin/python
# Start 
# Working on Pathlib again
# Module
from pathlib import Path 
import datetime


current = Path.cwd()

#for path in current.rglob("*"):
#    print(path.relative_to(current).parts)

time, file_path = max((f.stat().st_mtime, f) for f in current.iterdir())
#print(datetime.fromtimestamp(time), file_path)

lala = max((f.stat().st_mtime, f) for f in current.iterdir())
print(lala)

# End