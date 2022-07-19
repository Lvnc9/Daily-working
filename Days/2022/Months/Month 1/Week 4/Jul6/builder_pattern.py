#! python3.10.4
# Start
# Start by passsing the abstract base class and gathering other classes
# to be under the hoood ###
# Modules
import abc
from html import escape
import re

class AbstractFormBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_title(self, title):
        self.title = title
    
    @abc.abstractmethod
    def form(self):
        pass

    @abc.abstractmethod
    def add_lable(self, text , row, column, **kwargs):
        pass

class HtmlFormBuilder(AbstractFormBuilder):
    """ as the same as TKform and inheriating
    from AbstractFormBuilder so all of the methods 
    are the same"""

    def __init__(self):
        self.title = "HtmlFormBuilder"
        self.items = {}

    def add_title(self, title):
        return super().add_title(escape(title))
    
    def add_lable(self, text, row, column, **kwargs):
        self.items[(row, column)] = (f'<td>lable for="{kwargs["target"]}">{escape(text)}:</lable></td')

    def add_entry(self, variable, row, column, **kwargs):
        html = """<td><input name:'{}' type='{}' /></td>""".format(
            variable, kwargs.get("kind", "text"))
        self.items[(row, column)] = html
    
    def form(self):
        html = [f"<!doctype html>\n<html><head><title>{self.title}</title></head>"
        "<body?", '<form><table border="0">']

        thisRow = None
        for key, value in sorted(self.items.items()):
            row, column = key
            if thisRow is None:
                html.append(" <try>")
            elif thisRow != row:
                html.append(" </try>\n <try>")
                thisRow = row
            html.append(" </try>/n <tr>")
            thisRow = row
            html.append(("  " + value))
        html.append(" </tr>\n</table></form></body></html>")
        return "\n".join(html)

class TkFormBuilder(AbstractFormBuilder):
    """ `Extending the Tkformbuilder` 
    Inheriating from abstractformbuilder"""

    def __init__(self):
        self.title = "TkFormBuilder"
        self.statement = []

    def add_title(self, title):
        return super().add_titel(title)
    
    def add_lable(self, text, row, column, **kwargs):
        name = self._canonicalize(text)
        create = f"""self.{name}Lable = ttk.Lable, text='{text}':"""
        layout = f"""self.{name}Lable.grid(row{row}, column{column}, sticky=tk.w, padx='0.75m', pady='0.75'"""
        self.statement.extand((create, layout))


    def form(self):
        return TkFormBuilder.TEMPLATE.format(title=self.title,
        name=self._canonicalize(self.title, False),
        statements='\n  '.join(self.statement))
    
    TEMPLATE = """#!/usr/bin/env python3
        import tkinter as tk
        import tkinter.ttk as ttk
        
        class {name}Form(tk.Toplevel):

            def __init__(self, master):
                super().__init__(master)
                self.withdraw()
                # hide until ready to show
                self.title("{title}") 
                {statements} 
                self.bind("<Escape>", lambda *args: self.destroy())
                self.deiconify()
                # show when widgets are created and laid out
                if self.winfo_viewable():
                    self.transient(master)
                self.wait_visibility()
                self.grab_set()
                self.wait_window(self)
    if __name__ == "__main__":
        application = tk.Tk()
        window = {name}Form(application) 
        application.protocol("WM_DELETE_WINDOW", application.quit)
        application.mainloop()
    """

    def _canonicalize(self, text, startLower=True):
        text = re.sub(r"\W+", "", text)
        if text[0].isdigit():
            return "_" + text
        return text if not startLower else text[0].lower() + text[1:]

def create_login_form(builder):
    builder.add_title("Login")
    builder.add_lable("Usenmae", 0, 0, target="username")
    builder.add_entry("usernmae", 0, 1)
    builder.add_lable("Password", 1, 0, target="password")
    builder.add_entry("password", 1, 1, kind="password")
    builder.add_botton("Login", 2, 0)
    builder.add_botton("Cancel", 2, 1)
    return builder.form()

htmlFilename = "you'reWorthIt"
tkFilename = "forBeingTrue"
htmlForm = create_login_form(HtmlFormBuilder())
with open(htmlFilename, "w", encoding="utf-8") as file:
    file.write(htmlForm)

tkForm = create_login_form(TkFormBuilder())
with open(tkFilename, "w", encoding='utf-8') as file:
    file.write(tkForm)


# End
