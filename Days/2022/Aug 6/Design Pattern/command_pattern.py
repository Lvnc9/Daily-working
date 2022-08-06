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


class UndoGrid(Grid):

    def create_cell_command(self, x, y, color):
        def undo():
            self.cell(x, y, undo.color)

        def do():
            undo.color = self.cell(x, y)
            self.cell(x, y, color)
        return Command.command(do, undo, "Cell")
        
# End