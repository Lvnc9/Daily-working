#!/usr/bin/python
# Start
# Gravite game -> preferences part
# ---
import tkinter as tk
import tkinter.ttk as ttk


class Lala(tk.Frame):
    """ Something """

    def __init__(self, master=None):
        super().__init__(master)
        helloLabel = ttk.Label(self, text="Hello Sam",      # Showing messages
                foreground="green",
                background="#34A2FE")
        quicBotton = ttk.Button(self, text="Quit", command=self.quit) # Button for clicking
        nameButton = ttk.Entry(                 # entery adding info
                self,
                background="blue",
                foreground="red",
                width=50,
                )
        nameBox = tk.Text()     # a text box
        helloLabel.pack()
        quicBotton.pack()
        nameButton.pack()
        nameBox.pack()
        self.pack()
        #self.create_event()

window = Lala()
window.master.title("HELLLO")
window.master.mainloop()





# End