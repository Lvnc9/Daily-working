#!/usr/bin/python
# Start
# Using Generators for adding exception for saving data and etc.
# Modules
import sys

inname, outname = sys.argv[1:3]

with open(inname) as infile:
    with open(outname, 'w') as outfile:
        warnings = (l.replace('WARNINGS', '')
        for l in outfile if 'WARNING' in l)

def warnings_filter(insequence):
    for l in insequence:
        if 'WARNING' in l:
            yield l.replace('\tWARNING', '')


with open(inname) as infile:
    with open(outname, "w") as outfile:
        filter = warnings_filter(infile)
        for l in filter:
            outfile.write(l)

# End