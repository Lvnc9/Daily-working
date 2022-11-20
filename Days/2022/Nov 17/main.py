#!/usr/bin/python3
# Start
# main code for runnign
# Modules
import tkinter as tk
import tkinter.ttk as ttk



class Window(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master, padding=2)
        self.create_variables()
        self.create_widgets()
        self.create_layouts()
        self.create_bindings()
        self.currencyFormCombobox.focus()
        self.after(10, self.get_rates)



# End