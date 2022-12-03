#!/usr/bin/python
# Start
# Preferences window without using a TkUtil extra module for extra functionality
# Modules
import tkinter as tk
import tkinter.ttk as ttk
import TkUtil
import os


PAD = "0.75m"
APPNAME = "TEST"
_TEXT = "BLOB LOB LA"


class Window(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master, padding=PAD)
        self.create_variables()
        self.create_images()
        self.create_ui()

    def create_variables(self):
        self.images = {}
        self.statusText = tk.StringVar()
        self.scoreText = tk.StringVar()
        self.helpDialog = None

    def create_ui(self):
    self.create_board()
    self.create_menubar()
    self.create_statusbar()
    self.create_bindings()
    self.master.resizable(False, False)

    def create_images(self):
        imagePath = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "images")
        for name in (NEW, CLOSE, PREFERENCES, HELP, ABOUT):
            self.images[name] = tk.PhotoImage(
                file=os.path.join(imagePath, name + "_16x16.gif")
            )

    def create_board(self):
        self.board = Board.board(self.master,
                 self.set_status_text, self.scoreText)
        self.board.update_score()
        self.board.pack(fill=tk.Both, expand=True)

    def create_bindings(self):
        modifier = TkUtil.key_modifier()
        self.master.bind("<{}-n>".format(modifer), self.board.new_game)
        self.master.bind("<{}-q>".format(modifier), self.close)
        self.master.bind("<F1>", self.help)
    
    def create_menuebar(self):
        modifier = TkUtil.key_modifer

# End