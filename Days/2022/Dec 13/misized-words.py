#!/usr/bin/python
# Start
# misized words and customes
# Modules
import tkinter as tk
import tkinter.ttk as ttk


# Main class
class StickyAandB(tk.Tk):
    """ making a moving word """

    def moving_A_B(self):
        self.columnconfigure(0, minsize=250)
        self.rowconfigure([0, 1], minsize=100)

        lbl = tk.Label(text="A")
        lbl.grid(row=0, column=0, sticky="sw")
        
        lbl2 = tk.Label(text="B")
        lbl2.grid(row=1, column=0, sticky="ne")


class StickyColoredAandB(tk.Tk):

    def colored_A_B(self):
        self.columnconfigure(0, minsize=50)
        self.rowconfigure([0, 1, 2, 3], minsize=50)

        lbl1 = tk.Label(text="1", bg="black", fg="white")
        lbl2 = tk.Label(text="2", bg="black", fg="white")
        lbl3 = tk.Label(text="3", bg="black", fg="white")
        lbl4 = tk.Label(text="4", bg="black", fg="white")
        
        lbl1.grid(row=0, column=0)
        lbl2.grid(row=0, column=1, sticky="ew")
        lbl3.grid(row=0, column=2, sticky="ns")
        lbl4.grid(row=0, column=3, sticky="nsew")


if __name__ == "__main__":
    hmmm = Lala()
    hmmm.moving_A_B()
    hmmm.mainloop()






# End