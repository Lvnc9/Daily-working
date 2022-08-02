#!/usr/bin/python
# Start
# Unknown yet
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