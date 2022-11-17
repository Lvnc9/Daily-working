#!/usr/bin/python
# Start
# Using GUI libraries for making ui 
# Modules
import tkinter as tk
import tkinter.ttk as ttk


# hello world window
class Window(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master) # Creates self.master
        helloLabel = ttk.Label(self, text="Hello world")
        quitLabel = ttk.Button(self, text="Quit", command=self.quit)
        helloLabel.pack()
        quitLabel.pack()
        self.pack()

window = Window() # Implicity creates tk.Tk object
window.master.title("Hallo")
window.master.mainloop()







# End