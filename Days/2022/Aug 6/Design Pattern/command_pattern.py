#!/usr/bin/python
# Start
# How to idk from now but i can find a difinition for that if you pay attenrion ;?
# Modules
import code


class Grid:
    def __init__(self, width, height):
        self.__cells = [['white' for _ in (height)] 
                        for _ in (width)]
    
    def cell(self, x, y, color=None):
        if color is None:
            return self.__cells[x][y]
        self.__cells[x][y] = color

    @property
    def rows(self):
        return len(self.__cells[0])
    
    @property
    def columns(self):
        return len(self.__cells)


# End