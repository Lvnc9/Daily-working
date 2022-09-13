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

        self.small_trees = {
            "needs_water" : True,
            "thorns" : False,
            "need_music" : True,
            "fruite_given" : True,
            "leaf" : True,
            "wheter_changes" : True,
        }
        
        self.cactuses = {
        "needs_water" : True,
        "needs_music" : True,
        "thorns" : True, 
        "fruite_given" : False,
        "leaf" : False,
        "wheter_changes" : False,
        }
        
        self.stem_plants = {
        "needs_water" : True,
        "needs_music" : False,
        "thorns" : False,
        "fruite_given" : True,
        "leaf" : True,
        "wheter_changes" : True,
        }

# End