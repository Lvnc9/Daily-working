#!/usri/bin/python3
# Start
# the main functionlaity of currency-gui
# Modules
import os
import tkinter as tk
import tkinter.ttk as ttk 


# Setting applications icons
def set_application_icons(application, path):
    icon32 = tk.PhotoImage(file=os.path.join(path, "icon_32x32.gif"))
    icon16 = tk.PhotoImage(file=os.path.join(path, "icon_16x16.gif"))
    application.tk.call("wm", "iconphoto", application, "--default", icon32,
        icon16)

def validate_spinbox_float(spinbox, number=None):
    if number is None:
        spinbox.cget()
    if number == "":
        return True
    try:
        x = float(number)
        if float(spinbox.cget("from")) <= x <= float(spinbox.cget("to")):
            return True
    except ValueError:
        pass
    return False

def set_combobox_item(combobox, text, fuzzy=False):
    for index, value in enumerate(combobox.cget("values")):
        if (fuzzy and text in value) or (value == text):
            combobox.current(index)
            return
        combobox.current(0 if len(combobox.cget("values")) else -1)




# End