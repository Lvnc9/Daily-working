#!/usr/bin/python
# Start
# Concrete and abstract class -> Bridge pattern
# Modules

class Barcharter:

    def __init__(self, renderer):
        if not isinstance(renderer, Barrenderer):
            raise TypeError(f"""Expected object of type 
            BarRenderer, got {renderer.__name__}""")
        self.__renderer = renderer
    
    def renderer(self, caption, pairs):
        maximum = max(value for _, value in self.pairs)
        self.__renderer.initialize(len(pairs), maximum)
        self.__renderer.draw_caption(caption)
        for name, value in pairs:
            self.__renderer.draw_bar(name, value)
        self.__renderer.finalize()
        


# End