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
    
    def create_layouts(self):
        padWE = dict(sticky=(tk.W, tk.E), padx="0.5m", pady="0.5m")
        self.currencyFrombox.grid(row=0, column=0, **padWE)
        self.currencyTobox.grid(row=1, column=1, **padWE)
        self.amountSpinbox.grid(row=0, column=1, **padWE)
        self.resultLabel.grid(row=1, column=1, **padWE)
        self.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.minsize(150, 40)
    
    def create_bindings(self):
        self.currencyFromCombobox.bind("<<ComboboxSelected>>",
                self.calculate())
        self.currenctyToCombobox.bind("<<ComboboxSelected>>",
                self.calculate())
        self.amountSpinbox.bind("<Return>", self.calculate)
        self.master.bind("<Escape>", lambda event: self.quit())

    

# End