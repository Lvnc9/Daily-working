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

    def __init__(self, lbl_text):
        self.lbl_text = lbl_text
        self.label = tk.Label(master=self, text=lbl_text)
        self.label["text"] = "Good bye"
        lbl_value = tk.Label(master=self, text="0")
        lbl_value.grid(row=0 column=1)
    
    text = lbl_text["text"]
    lbl_value = tk.Label(master=StickyColoredAandB(), text="0")
    lbl_value.grid(row=0, column=1)
    # Increase decrease funcitons
    @classmethod
    def increase(cls):
        value = int(cls.lbl_value["text"])
        cls.lbl_value["text"] = f"{value + 1}"

    @classmethod
    def decrease(cls):
        value = int(cls.lbl_value["text"])
        cls.lbl_value["text"] = f"{value - 1}"

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

    def increase_decrease_buttons(self):

        self.columnconfigure(0, minsize=50, weight=1)
        self.rowconfigure([0, 1, 2], minsize=50, weight=1)

        btn_increase = tk.Button(master=self, text="+", command=self.increase())
        btn_increase.grid(row=0, column=0, sticky=tk.BOTH)

        btn_decrease = tk.Button(master=self, text="-", command=self.decrease())
        btn_decrease.grid(row=0, column=2, sticky=tk.BOTH)
            


if __name__ == "__main__":
    #hmmm = StickyAandB()
#    hmmm.moving_A_B()
#    hmmm.mainloop()
    hmmm2 = StickyColoredAandB()
    hmmm2.colored_A_B()
    hmmm2.mainloop()





# End