#!/usr/bin/python
# Start
# Gravite game -> preferences part
# ---
import tkinter as tk
import tkinter.ttk as ttk


class Lala(tk.Frame):
    """ Something """

    boarder_effects = {
        "flat" : tk.FLAT,
        "sunken" : tk.SUNKEN,
        "raised" : tk.RAISED,
        "groove" : tk.GROOVE,
        "ridge" : tk.RIDGE,
    }

    def __init__(self, master=None):
        super().__init__(master,)
        helloLabel = ttk.Label(self, text="Hello Sam",      # Showing messages
                relief=tk.SUNKEN,
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

#window = Lala()
#window.master.title("HELLLO")
#window.master.mainloop()

window = tk.Tk()
frame = tk.Frame()
#lbl = tk.Label(master=frame, text='Something', relief=tk.SUNKEN).pack()
ent = tk.Entry(master=frame, relief=tk.GROOVE, width=100)
ent.insert(tk.END, "What is you're name? ")
btn = tk.Button(master=frame, text="Quit", relief=tk.SUNKEN, command=frame.quit)
ent.pack()
btn.pack()
frame.place
frame.pack()

window.mainloop()




# End