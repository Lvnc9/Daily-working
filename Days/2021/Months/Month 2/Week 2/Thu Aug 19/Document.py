#! python3.9.2
# Start
# An Document app that do the basic things of a document
# TODO Modules

# Basic thing of the Document
class Document:
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''
    
    def insert(self, character):
       if not hasattr(character, 'character'):
           character = Character(character)
       
        #self.characters.insert(self.cursor.position, character)
        #self.cursor.forward()

    def delete(self):
        del self.characters[self.cursor.position]
    
    def save(self):
        with open(self.filename, 'w') as file:
            file.write(''.join(self.characters))

    @property
    def string(self):
        return "".join(str(c) for c in self.characters)
# Expending Cursor for abling to make more decisian :l
class Cursor:
    """ Expending cursor attr to make the cursor more wide for
    accepting another keys from the keyboard """

    def __init__(self, document:object):
        self.document = document
        self.position =  0
    
    def forward(self):
        self.position += 1
    
    def back(self):
        self.position -= 1
    
    def home(self):
        "Back the cursor to the start of the line"
        if self.document.characters == 0:
            return None

        while self.document.characters[
                self.position-1].character != '\n':
            self.position -= 1
            if self.position == 0:
                "Reaches to 1 place of the lines"
                break
    
    def end(self):
        "Go to the lastest characters cursor"

        while self.position < len(self.document.characters
        ) and self.document.characters[
            self.position].character != '\n':
            self.position += 1

class Character:
    """ Expand the main characters attr to add features as
    bold, underline and italic """

    def __init__(self, character, 
            bold=False, italic=False, underline=False):
        assert len(character) == 1, "Length of the character is to tall"
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline
    
    def __str__(self):
        bold = "*" if self.bold else ""
        italic = "/" if self.italic else ""
        underline = "_" if self.underlin else ""
        return bold + italic + underline + self.character

# End