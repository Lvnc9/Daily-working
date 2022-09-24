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

_un_load = _LibHyphen.hnj_hyphen_free
_un_load.argtypes = [ctypes.c_void_p]
_un_load.restype = None





# End