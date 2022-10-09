#!/usr/bin/python
# Start
# reLearning pathlib
# Modules
import pathlib


path = pathlib.PureWindowsPath(r"C:\Users\lalamo\realSam\test.txt")

print(path.parent)



rechangedPath = pathlib.Path("C:\Users\lalamo\realSam\test.txt")
print(rechangedPath)
# End