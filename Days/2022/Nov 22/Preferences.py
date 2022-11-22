#!/usr/bin/python
# Start
# Modal preferences dialog 
# Modules
import tkinter as tk
import tkinter.ttk as ttk
import TkUtil


class Window(TkUtil.Dialog):

    def __init__(self, master, board):
        self.board = board
        super().__init__(master, f"Preferences \u2014 {APPNAME}",
                TkUtil.OK_BUTTON|TkUtil.CANCEL_BUTTON)
        
    def body(self, master):
        self.create_varialbes()
        self.create_widgets(master)
        self.create_layout()
        self.create_bindings()
        return self.frame, self.columnSpinbox

    def create_variables(self):
        self.columns = tk.StringVar()
        self.columns.set(self.board.columns)
        self.rows = tk.StringVar()
        self.rows.set(self.board.rows)
        self.maxColors = tk.StringVar()
        self.maxColors.set(self.board.maxColors)
    
    


# End