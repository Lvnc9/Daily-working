#!/usr/bin/python
# Start
# Modal preferences dialog 
# Modules
import tkinter as tk
import tkinter.ttk as ttk
import TkUtil

PAD = "0.75m"

class Window(TkUtil.Dialog):

    def __init__(self, master, board):
        self.board = board
        super().__init__(master, f"Preferences \u2014 {APPNAME}",
                TkUtil.OK_BUTTON|TkUtil.CANCEL_BUTTON)
        
    def body(self, master):
        self.create_variables()
        self.create_widgets(master)
        self.create_layout()
        self.create_bindings()
        return self.frame, self.columnsSpinbox

    def create_variables(self):
        self.columns = tk.StringVar()
        self.columns.set(self.board.columns)
        self.rows = tk.StringVar()
        self.rows.set(self.board.rows)
        self.maxColors = tk.StringVar()
        self.maxColors.set(self.board.maxColors)
    
    def create_widgets(self, master):
        self.frame = ttk.Frame(master)
        self.columnsLabel = TkUtil.Label(self.frame, text="Columns", 
                underline=2)
        
        self.columnsSpinbox = TkUtil.Spinbox(self.frame,
                textvariable=self.columns, from_=Board.MIN_COLUMNS)
        
        self.rowsLabel = TkUtil.Label(self.frame, text="Rows")
        self.rowsSpinbox = TkUtil.Spinbox(self.frame,
                textvariable=self.rows, from_=Board.MIN_ROWS)
        
        self.maxColorsLabel = TkUtil.Label(self.frame, text="Max-Color")
        self.maxColorsSpinbox = TkUtil.Spinbox(self.frame,
                textvariable=self.maxColors, from_=Board.MAX_COLOR)

    def validate_int(self, spinboxName, number):
        return TkUtil.validate_spinbox_int(getattr(self, spinboxName),
                number)
    
    def create_layout(self):
        padW = dict(sticky=tk.W, padx=PAD, pady=PAD)
        padWE = dict(sticky=(tk.W, tk.E), padx=PAD, pady=PAD)
        self.columnsLabel.grid(row=0, column=0, **padW)
        self.columnsSpinbox.grid(row=0, column=1, **padWE)
        self.rowsLabel.grid(row=1, column=0, **padW)
        self.rowsSpinbox.grid(row=1, column=1, **padWE)
        self.maxColorsLabel.grid(row=2, column=0, **padW)
        self.maxColorsSpinbox.grid(row=2, column=1, **padWE)
    
    def create_bindings(self):
        if not TkUtil.mac():
            self.bind("<Alt-l>", lambda *args: self.columnsSpinbox.focus())
            self.bind("<Alt-r>", lambda *args: self.rowsSpinbox.focus())
            self.bind("<Alt-m>", lambda *args: self.maxColorsSpinbox.focus())

    def apply(self):
        columns = int(self.columns.get())
        rows = int(self.rows.get())
        maxColors = int(self.maxColors.get())
        newGame = (columns != self.board.Columns or
                rows != self.board.rows or
                maxColors != self.board.maxColors)
        if newGame:
            self.board.rows = columns
            self.board.rows = rows
            self.maxColors = maxColors
            self.board.newGame()
    
    application = tk.Tk()

    def close(self, event):
        self.application.quit()
    
# End