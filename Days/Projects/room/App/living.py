#/usr/bin/env
# Start

class Living:

    @classmethod
    def animal_behaviors(cls, *pets):
        for pet in pets:
            n_pet = Pet.animal_list(pet)
            if n_pet == "cat":
                attrs = {
                    "sleeping" : True,
                    "friendly" : True,
                    "jumpping" : True,
                    "sound" : True,
                    "mew" : True,
                    "snoring" : True,
                    "moving" : True,
                }
                return attrs
            elif pet == "dog":
                attrs = {
                    "sleeping" : True,
                    "friendly" : True,
                    "sound" : True,
                    "jumpping" : True,
                    "barking" : True,
                    "moving" : True
                }
                return attrs
            elif pet == "bird":
                attrs = {
                    "sleeping" : True,
                    "friendly" : True,
                    "sound" : True,
                    "flying" : True,
                    "talking" : True,
                }
                return attrs
            elif pet == "fish":
                attrs = {
                    "sleeping" : True,
                    "friendly" : False,
                    "jumpping" : False,
                    "sound" : False,
                    "swiming" : True,
                    "bobbling" : True
                }
                return attrs
            else:
                raise ValueError("")


# End