#!/usr/bin/python
# Start
### we have Kernel linux log that tells us hard is broken
# and we find hard disk logs to find the right errors that had been eccured
# so we write a programm that uses coroutines to find the right serinal number 
# and bus Identifier (0:0:0:0) and a sda block device identifier (sda) of the hard disk
# and separate write it in another log file ###
# Modules
import re
 

def match(filename, regex):
    with open(filename) as file:
        lines = file.readlines()
    for line in reversed(lines):
        match = re.match(regex, line)
        if match:
            # this yield is used for finding next importent line
            regex = yield match.groups()[0]

def get_serials(filename):
    ERROR_RE = "XFS ERROR (\[sd[a-z]\])"
    matcher = match(filename, ERROR_RE)
    device = next(matcher)
    while True:
        bus = matcher.send(
            "(sd \S+) {}.*".format(re.escape(device)))
        serial = matcher.send("{} \ (SERIAL=([^)]*)\)".format(bus))
        # This yield is used to decide which lines is importent
        yield serial
        device = matcher.send(ERROR_RE)

with open('EXAMPLE_LOG.log') as log:
    with open('XFS_SEPARATED.log', 'w') as xfsWriter:
        for serial_number in get_serials(log):
            print(serial_number)
            xfsWriter.write(serial_number)


# End