#!/usr/bin/python
# Start
# Working on Generators 
# Modules
import sys


infile, outfile = sys.argv[1:3]

with open(infile) as infile:
    with open(outfile, 'w') as outfile:
        warnings = (l.replace('WARNINGS', '')
        for l in outfile if 'WARNING' in l)
        
        outfile.write(outfile)


# A bad Looking code as example of using generators as using OOP
class WarningFilter:
    """ Filters the Warning lines 
    and replace them with a ' ' """

    def __init__(self, insequence):
        self.insequence = insequence
    
    def __iter__(self):
        return self

    def __next__(self):
        l = self.insequence.readline()
        while 'WARNING' and l not in l:
            l = self.insequence.readline()
        if not l:
            raise StopIteration
        return l.replace('\tWARNING', '')

with open(infile) as inname:
    with open(outfile, 'w') as outfile:
        filters = WarningFilter(infile)
        for line in filters:
            outfile.write(line)


def warning_filter(insequences):
    for l in insequences:
        if 'WARNING' in l:
            yield l.replace('WARNING', '')

with open(infile) as inname:
    with open(outfile, 'w') as outname:
        filter = warning_filter(infile)
        outfile.write(filter)




# End