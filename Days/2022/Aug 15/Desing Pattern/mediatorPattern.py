#!/usr/bin/python
# Start
# we want to use mediator object in this file and it encapsulate 
# the interaction between other objects
# Modules
from collections import defaultdict

class Form:

    def __init__(self):
        self.create_widget = create_widget()
        self.create_mediator = create_mediator()
    
    def create_widget(self):
        self.name_text = Text()
        self.email_text = Text()
        self.ok_button = Button("OK")
        self.cancel_button = Botton("CANCEL")
    
    def create_medator(self):
        self.mediator = Mediator((self.name_text, update_ui),
                                (self.email_text, update_ui),
                                (self.ok_button, self.clicked),
                                (self.cancel_button, self.clicked))
        self.update_ui()

    def update_ui(self, widget=None):
        self.ok_button.enabled = (bool(self.name_text) and
                                  bool(self.email_text))
    
    def clicked(self, widget):
        if widget == self.ok_button:
            print("OK")
        elif widget == self.cancel_button:
            print("Cancel")

    
    class Mediator:
        
        def __init__(self, widgetCallablePairs):
            self.callable_for_widgets = defaultdict(list)
            for widget, caller in widgetCallablePairs:
                self.callablesForWidget[widget].append(caller)
                widget.mediator = self



# End