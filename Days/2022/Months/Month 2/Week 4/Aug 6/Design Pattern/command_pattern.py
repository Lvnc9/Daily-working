#!/usr/bin/python
# Start
# How to idk from now but i can find a difinition for that if you pay attenrion ;?
# Modules



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

    def create_rectangle_macro(self, x0, x1, y0, y1, color):
        macro = Command.Macro("Rectangle")
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                macro.add(self.create_cell_command(x, y, color))
        return macro


class Command:
    def __init__(self, do, undo, description=""):
        assert callable(do) and callable(undo)
        self.do = do 
        self.undo = undo
        self.description = description
    
    def __call__(self):
        self.do()

class Macro:
    def __init__(self, description):
        self.description = description
        self.__commands = []

    def add(self, command):
        if not isinstance(command, Command):
            raise TypeError(f"Expected Object at {type(command).__name__}")
        self.__commands.append(command)

    def __call__(self):
        for command in self.__commands:
            command()
    
    do = __call__

    def undo(self):
        for command in reversed(self.__commands):
            command.undo()
# End