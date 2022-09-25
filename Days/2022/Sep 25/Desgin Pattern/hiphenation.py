#!/usr/bin/python
# Start
# Working on Unknown
# Modules
import ctypes

class Error(Exception): pass
_libraryName = ctypes.util.find_library("hyphen")
if _libraryName is None:
    _libraryName = ctypes.util.find_library("hyphen.uno")
if _libraryName is None:
    raise Error("cannot find hyphenation library")

_LibHyphen = ctypes.CDLL(_libraryName)

_load = _LibHyphen.hnj_hyphen_load
_load.argtypes = [ctypes.c_char_p]      # const char *filename
_load.restype = ctypes.c_void_p         # HyphenDict *
_LibHyphen = ctypes.CDLL(_libraryName)


_unload = _LibHyphen.hnj_hyphen_free
_unload = [ctypes.c_void_p]     # Hyphendict *hdict
_unload.restype = None





# End