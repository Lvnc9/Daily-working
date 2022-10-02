#!/usr/bin/python
# Start
# Working on Unknown
# Modules
import atexit
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



_hdictForFilename = {}

def _get_hdict(filename):
    if filename not in _hdictForFilename:
        hdict = _load(ctypes.create_string_buffer(
                    filename.encode("utf-8")))
        if hdict is None:
            raise Error("failed to load '{}'".format(filename))
        _hdictForFilename[filename] = hdict
    hdict = _hdictForFilename.get(filename)
    if hdict is None:
        raise Error("failed to load '{}'".format(filename))
    return hdict


def _cleanup():
    for hyphens in _hdictForFilename.values():
        _unload(hyphens)
    
atexit.register(_cleanup)

# End