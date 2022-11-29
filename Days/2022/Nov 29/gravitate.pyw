#!/usr/bin/python
# Start
# Gravite game ->
# ----
# Modules
import tkinter as tk
import tkinter.ttk as ttk
import TkUtil
import os
import Main


APPNAME = "LALA LOYA"



def main():
    application = tk.Tk()
    application.withdraw()
    application.title(APPNAME)
    application.option_add("*tearOff", False)
    TkUtil.set_application_icons(
        application, os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "images"
            ))
    window = Main.Window(application)
    application.protocol("WM_DELETE_WINDOW", window.close)
    application.deiconify()
    application.mainloop()
    

# End