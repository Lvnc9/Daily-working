#!/usr/bin/python
# Start
# Setup 
# Modules
import distutils
import cython


distutils.core.setup(name="Hyphenate2",
    cmdclass={"build_ext": cython.Distutils.build_ext},
    ext_modules=[distutils.extension.Extension("Hyphenate",
        ["Hyphenate.pyx"], libraries=["hyphen"])])
