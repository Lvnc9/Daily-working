#!/usr/bin/python
# Start
# Setup 
# Modules
from distutils.command.build_ext import build_ext
import cython
import setuptools
import hyphenate
setuptools.setup(name="Hyphenate2",
    cmdclass={"build_ext": build_ext},
    ext_modules=[setuptools.Extension("Hyphenate",
        ["Hyphenate.pyx"], libraries=["hyphen"])])



# End