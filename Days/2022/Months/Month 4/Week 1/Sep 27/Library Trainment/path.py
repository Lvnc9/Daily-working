#!/usr/bin/python
# Start
# Learning
# Modules
from pathlib import Path


def unique_path(dire, name_pattern):
    counter = 0

    while True:
        counter += 1
        path = dire / name_pattern.format(counter)
        if not path.exists():
            return path

path = unique_path(Path.cwd(), "test {:03d}.text")
print(path)



# End