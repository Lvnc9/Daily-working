#!/usr/bin/python
# Start 
# Faster running time with cython
# Modules
import ctypes


class Error(Exception): pass


_libraryName = ctypes.util.find_library("hyphen")
if _libraryName is None:
    _libraryName = ctypes.util.find_library("hyphen.uno")
if _libraryName is None:
    raise Error("cannot find hyphenation library")


_LibHyphen = ctypes.cdll(_libraryName)




# End