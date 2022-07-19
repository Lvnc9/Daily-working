#! python3.9.2
# Start
# Learning the new 'pathlib' library that takes the place of os.path :/
# Modules
import pathlib
import os

os.chdir("./Days/Sat Aug 7")
#path = pathlib.Path.cwd().joinpath("Days", "Sat Aug 7", "idk.txt").read_text()
print(pathlib.Path("idk.txt").read_text())

print('and now i have a laptop that i can work with and see some pashmaki things')


# End