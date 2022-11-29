#!/usr/bin/python
# Start
# Preferences window without using a TkUtil extra module for extra functionality
# Modules
import tkinter as tk
import tkinter.ttk as ttk
import TkUtil


PAD = "0.75m"
APPNAME = "TEST"
_TEXT = "BLOB LOB LA"


class Window(tk.Toplevel):
    
    def __init__(self, master):
        super().__init__(master)
        self.withdraw()
        self.title("Help \u2014 {}".format(APPNAME))
        self.create_ui()
        self.reposition()
        self.resizable(False, False)
        self.deiconify()
        if self.winfo_viewable():
            self.transient(master)
        self.wait_visibility()
    
    def create_ui(self):
        self.helpLabel = ttk.Label(self, text=_TEXT, background="white")
        self.closeButton = TkUtil.Button(self, text="Close", undeline=0)
        self.helpLabel.pack(anchor=tk.N, expend=True, fill=tk.BOTH,
                padx=PAD, pady=PAD)
        self.closeButton.pack(anchor=tk.S)
        self.protocol("WM_DELETE_WINDOW", self.close)
        if not TkUtil.mac():
            self.bind("<Escpae>", self.close)
            self.bind("<Escape>", self.reposition)
    
    def reposition(self, event=None):
        if self.master is not None:
            self.geometry("+{}{}".format(
                    self.master.winfo_rootx() + 50,
                    self.master.winfo_rooty() + 50))
                
    def close(self, event):
        self.withdraw()  
    
    application = tk.Tk()

# End