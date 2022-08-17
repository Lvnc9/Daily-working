#!/usr/bin/python
# Start
# Making an Mediator Object usig coroutines and chaincalls
# Moduels:
from functools import wraps

# For convertingg Generators inside form to coroutines using decorators
def coroutine(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        generator = func(*args, **kwargs)
        next(generator)
        return generator
    return wrapper


class Form:

    def __init__(self):
        self.create_mediator()
        self.create_widget()

    def create_widget(self):
        self.nameText = Text()
        self.emailText = Text()
        self.okButton = Button("OK")
        self.cancelBotton = Button("Cancel")

    def create_mediator(self):
        self.mediator = self._update_ui_mediator(self.clicked_mediator())
        for widget in (self.nameText, self.emailText,
                       self.okButton, self.cancelBotton):
            widget.mediator = self.mediator
        self.mediator.send(None)

    @coroutine
    def _update_ui_mediator(self, successor=None):
        # one of the good usages of this update_ui is making the code shorter
        # and the written is less complex and more usefull
        while True:
            widget = yield
            self.okButton.enabled = (bool(self.nameText) and
                                     bool(self.email_text))
            if successor is not None:
                successor.send(widget)

    @coroutine
    def clicked_mediator(self, successor=None):
        while True:
            widget = yield
            if widget == self.okButton:
                print("OK")
            elif widget == self.cancelBotton:
                print("Cancel")
            elif successor is not None:
                successor.send(widget)


class Mediated:
    
    def __init__(self):
        self.mediator = None
    
    def on_change(self):
        if self.mediator is not None:
            self.mediator.send(self)

class Button(Mediated):

    def __init__(self, text=""):
        super().__init__()
        self.text = text
        self.enabled = True
    
    def clicked(self):
        if self.enabled:
            self.on_change()


class Text(Mediated):

    def __init__(self, text=""):
        super().__init__()
        self.__text = text
    
    @property
    def text(self):
        return self.__text
    
    @text.setter
    def text(self, text):
        if self.text != text:
            self.__text = text
            self.on_change()
        
# End