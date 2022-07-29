#!/usr/bin/python
# Start
# Some examles of using yield generator for iterating files
# Moduels
import sys


# Seperating inputes from inputs
inname, outname = sys.argv[1:3]


# Not Readable enough but look at it
def warning_filter(infilename):
    with open(infilename) as infile:
        yield from (
            l.replace('\tWARNING', '')
            for l in infile
            if 'WARNING' in l
        )

filter = warning_filter(inname)
with open(outname, 'w') as outfile:
    outfile.write(filter)

class Folder:
    pass


def walk(file):
    if isinstance(file, Folder):
        yield file.name + '/'
        for f in file.children:
            yield from walk(f)
    else:
        yield file.name


# End