#!/usr/bin/python
# Start
# The Userinterface works for the command line
# Modules
import os
from pathlib import Path
import time
import backend
import sys 

# Base class
class UserInterface:
    # shower
    def shower(self):
        # Amir will add
        print("Welcome to the xfsFinder app ;)")
        print('')

    def loading(self):
        for lala in range(3):
            print('.', end="")
            time.sleep(1)
    # Mover

    def file_cheker(self):
        print('is the file exists at the current dir? y/n')
        current_dir_answer = str(input().lower())

        # absoloute path cheker
        if current_dir_answer == 'y':
            print("Enter the absolute path of the log file")
            self.__infilename = str(input())
            if not os.path.isfile(self.__infilename):
                raise FileNotFoundError("pleas enter a valid filename")
        else:
            sys.exit()
    def xfs_finder(self):
        print("pleas enter the output file [example.log]")
        outputFile = str(input())
        if not '.log' in outputFile:
            outputFile.join('.log')
        with open(self.__infilename) as log:
            with open(outputFile, 'w') as xfsWriter:
                for serial_number in backend.get_serials(log.readlines()):
                    print(serial_number)
                    xfsWriter.write(serial_number)
        print('Serial numbers have been written! ')

# End