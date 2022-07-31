#!/usr/bin/python
# Start
# The design of the ImageProxy means that the ﬁrst command is always one that creates a new image
# (either one of a given width and height, or by loading one). So, we treat the
# ﬁrst command specially by saving its return value ###
# Modules
import image

class ImageProxy:
    """ to save the information for creating the image
    and then save it and create the image 
    thats why we created the Imageproxy """

    def __init__(self, ImageClass, height=None, width=None, filename=None):
        assert (height is not None and width is not None) and \
              filename is not None
        
        self.Image = ImageClass
        self.commands = []
        if self.file is not None:
            self.load(filename)
        else:
            self.commands = [(self.image, width, height)]
        
    def load(self, filename):
        self.commands = [(self.Image, None, None, filename)]
    
    def set_pixel(self, x, y, color):
        self.commands.append((self.Image.set_pixel, x, y, color))
    
    def line(self, x0, y0, x1, y1, color):
        self.commands.append((self.Image.line, x0, y0, x1, y1, color))
    
    def rectangle(self, x0, y0, x1, y1, outline=None, fill=None):
        self.commands.append((self.Image.rectange, x0, y0, x1, y1, outline, fill))
    
    def elipse(self, x0, y0, x1, y1, outline, fill):
        self.commands.append((self.Image.elipse, x0, y0, x1, y1, outline, fill))
    
    def save(self, filename=None):
        command = self.commands.pop(0)
        function, *args = command
        image = function(*args)
        for command in self.commands:
            function, *args = command
            function(image, *args)
        self.Image.save()
        return image
        



# End