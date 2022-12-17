#!/usr/bin/python
# Start
# Notebook app using tkinter
# Modules
import tkinter as tk



# main 
class Notebook(tk.Tk):
    """ notebook app a main text widget with saving,
        loading, rmeoving buttons """


    def notebook(self):
        text_edit = tk.Text(self)
        frm_buttons = tk.Frame(master=self, relief=tk.RAISED, bd=2)
        btn_open = tk.Button(master=frm_buttons, text="open")
        btn_save = tk.Button(master=frm_buttons, text="Save As...")

        btn_open.grid(column=0, row=0, sticky="ew", padx=5, pady=5)
        btn_save.grid(column=0, row=1, sticky="ew", padx=5)

        frm_buttons.grid(row=0, column=0, sticky="ns")
        text_edit.grid(row=0, column=1, sticky="nsew")

lala = Notebook()
lala.rowconfigure(1, minsize=800, weight=1)
lala.columnconfigure(1, minsize=800, weight=1)
lala.notebook()
lala.mainloop()





# End