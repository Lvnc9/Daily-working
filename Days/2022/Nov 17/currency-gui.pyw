#!/usr/bin/python
# Start
# Using TKinter -> working with GUI
# Modules
import tkinter as tk
import tkinter.ttk as ttk 
import tkutil
import os


# main -> running 
def main():
    application = tk.Tk()
    application.title("Currency")
    tkutil.set_application_icons(application, os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "images"))
    Main.window(application)
    application.mainloop()





# End