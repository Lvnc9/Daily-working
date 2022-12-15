#!/usr/bin/python
# Start
# Converting fahrenheit to celsius with GUI
# Modules
import tkinter as tk
import tkinter.ttk


# Fhare
class FahrenheitToCelsius(tk.Tk):

    def __init__(self):
        self.title("Temperature Converter")
        self.resizable(width=False, height=False)

    @classmethod
    def fahrenheit_to_celsius(cls, entry, lbl):
        """ Converts the value of Fahrenheit to Celsius
        and put the results into lbl_results """
        fahrenheit = entry.get()
        celsius = (5 / 9) * (float(fahrenheit) - 32)
        lbl["text"] =  f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

    def converter(self): 
        frm_entry = tk.Frame(master=self)
        ent_temperature = tk.Entry(master=frm_entry, width=10)
        lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
        
        ent_temperature.grid(column=0, row=9, sticky="e")
        lbl_temp.grid(column=0, row=1, sticky="w")

        btn_converter = tk.Button(
                master=self,
                text="\N{RIGHTWARDS BLACK ARROW}"
                command=FahrenheitToCelsiou(ent_temperature, lbl_results)
        )
        
        lbl_results = tk.Label(
            master=self,
            text="\N{DEGREE CELSIUS}"
        )

        frm_entry.grid(column=0, row=0, padx=10)
        btn_converter.grid(column=1, row=0, pady=10)
        lbl_results.grid(column=2, row=0, padx=10)


# End