#!/usr/bin/python
# Start
# An silly test for skipping py.test tester
# Modules
import sys
import py.test


def test_simple_skip():
    if sys.platform != "fackOS":
        py.test.skip("test works only in fakceOS")
    
    Fakeos.do_something_fake()
    assert Fakeos.did_not_haapen

class Fakeos: pass



# End