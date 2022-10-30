#!/usr/bin/python
# Start
# testing the code
# Modules
import pprint


lala = {
    "name" : "someone",
    "fname" : "anotherone"
}
alal = {
    "car" : "optical",
    "color"  : "yellow"
}


pashmak = {**lala, **alal}
pprint.pprint(pashmak)

# End