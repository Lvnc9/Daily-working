#! python3.9.2
# Start
# Propebloy writing the asked program of chapter 5 of OOP boock
# TODO: Modules

class Document:
    """ Head class of document app whos connect
    other classes of documentaion together """

    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character:str):
        self.characters.insert(self.cursor.position, character)
        self.cursor.position += 1

    def deletion(self):
        del self.characters[self.cursor] 
    
    def save(self):
        with open(self.filename, 'w') as file:
            file.write("".join(self.characters))
        
    @property
    def string(self):
        return  "".join(self.characters)

class Cursor():
    """ Expand the cursors abillity """

    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        self.position += 1

    def back(self):
        self.position -= 1

    def home(self):
        """ Back the position of curosr to the start of
        the line/file """

        if len(self.document.characters) <= 1:
            raise Exception("You should write something first")

        while self.document.characters[
                self.position-1] != '\n':
            self.position -= 1
            if self.position == 0:
                # Got to end of the line
                break
        
    def end(self):
        """ move to the position of cursor to the last
        character that inserted   """
        
        if len(self.document.characters) <= 1:
            raise Exception("You should write something first")
        
        while self.position < len(self.document.characters
                ) and self.position != '\n':
            self.position += 1
    
class Character:
    """ Charactrise the characters to make them
    bold-normal-italic-underlined """

    def __init__(self, character,
            bold:False, underline:False, italic:False):
        assert len(character) == 1, 'character is more than 1 letter'
        self.character = character
        self.bold = bold
        self.underline = underline
        self.italic = italic
    
    def __str__(self):
        pass




# End