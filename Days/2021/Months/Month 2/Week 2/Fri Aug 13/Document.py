#! python3.9.2
# Start
# An Document app that do the basic things of a document
# TODO Modules

# Basic thing of the Document
class Document:
    def __init__(self):
        self.characters = []
        self.cursor = 0
        self.filename = ''
    
    def insert(self, character):
        self.characters.insert(self.cursor, character)
        self.cursor += 1

    def delete(self):
        del self.characters[self.cursor]
    
    def save(self):
        with open(self.filename, 'w') as file:
            file.write(''.join(self.characters))

    def forward(self):
        self.cursor += 1
    
    def back(self):
        self.cursor -= 1


class Cursor:
    """ expend the cursor attr to make a better versiaty 
    for supporting Home and ... keys """

    def __init__(self, document):
        self.document = Document
        self.position = 0

    def forward(self):
        self.position += 1
    
    def back(self):
        self.position -= 1

    def home(self):
        while self.document.characters[
            self.position-1] != '\n':
            self.position -= 1
            if self.position == 0:
                # Got to the begging of the line
                break


# End