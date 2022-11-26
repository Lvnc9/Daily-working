#!/usr/bin/python
# Start
# Preferences window without using a TkUtil extra module for extra functionality
# Modules
import tkinter as tk
import tkinter.ttk as ttk


class Window(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.withdraw()
        self.title("Help \u2014 {}".format(APPNAME))
        self.create_ui()
        self.reposition()
        self.resizable(False, False)
        self.deiconify()
        if self.winfo_viewable():
            self.transient(master)
            self.wait_visibility()
    





# End