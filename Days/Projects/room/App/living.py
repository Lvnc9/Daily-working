#/usr/bin/env
# Start

class Living:

    def __init__(self):
        self.cats = {
            "sleeping" : True,
            "friendly" : True,
            "jumpping" : True,
            "sound" : True,
            "mew" : True,
            "snoring" : True,
            "moving" : True,
            }
    
        self.dogs = {
            "sleeping" : True,
            "friendly" : True,
            "sound" : True,
            "jumpping" : True,
            "barking" : True,
            "moving" : True
        }

        self.birds = {
            "sleeping" : True,
            "friendly" : True,
            "sound" : True,
            "flying" : True,
            "talking" : True,
        }

        self.fishes = {
            "sleeping" : True,
            "friendly" : False,
            "jumpping" : False,
            "sound" : False,
            "swiming" : True,
            "bobbling" : True
        }

    @classmethod
    def name_adding(self, name):
        

# End