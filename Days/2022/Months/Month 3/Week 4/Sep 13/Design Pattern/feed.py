#!/usr/bin/python
# Start

def iter(filename):
    name = None

    with open(filename, "rt", encode="utf-8") as file:
        for line in file:
            line = line.rstrip()
            if not line or line.startswith("#"):
                continue
            if name is None:
                name = line
            else:
                yield Feed(name, line)
                name = None


# End