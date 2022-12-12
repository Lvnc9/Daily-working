#!/usr/bin/python
# Start
# tkinter.Tk as head and multiple frames
# Modules
import tkinter as tk
import tkinter.ttk as ttk



# Head widget
class TK(tk.Tk):
    """ Head class holding multiple frames """

    def table(self):
        for i in range(3):
            for j in range(3):
                frame = tk.Frame(
                    master=self,
                    relief=tk.RAISED,
                    borderwidth=1
                )
                frame.grid(row=i, column=j, padx=5, pady=5)
                label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
                label.pack(padx=5, pady=5)

lala = TK()
lala.table()
lala.mainloop()





# End