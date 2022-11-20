#!/usr/bin/python3
# Start
# main code for runnign
# Modules
import tkinter as tk
import tkinter.ttk as ttk
import TkUtil

# spinbox 
spinbox = ttk.Spinbox if hasattr(ttk, 'Spinbox') else tk.Spinbox

# main code for running program
class Window(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master, padding=2)
        self.create_variables()
        self.create_widgets()
        self.create_layouts()
        self.create_bindings()
        self.currencyFormCombobox.focus()
        self.after(10, self.get_rates)

    def create_variables(self):
        self.currencyFrom = tk.StringVar()
        self.currencyTo = tk.StringVar()
        self.amount = tk.StringVar()
        self.rates = {}

    def create_widgets(self):
        self.currencyFrombox = ttk.Combobox(self,
                textvariable=self.currencyFrom)
        self.currencyTobox = ttk.Combobox(self,
                textvariable=self.currencyTo)
        self.amountSpinbox = spinbox(self, textvariable=self.amount,
                from_=1.0, to=10e6, validate="all", format="%0.2f",
                width=8)
        self.amountSpinbox.config(validatecommand=(
                self.amountSpinbox.register(self.validate), "%P"))
        
    def validate(self, number):
        return TkUtil.validate_spinbox_float(self.amountSpinbox, number)
    
    


# End