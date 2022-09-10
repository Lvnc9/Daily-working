#!/usr/bin/env
# Start
# MAC Module
# Modules
import logMac
import collections 
import pprint


# Logging with locMac Module
logger = logMac.LogWriter()
logger.file_name = "mac_loger.log"


def pprinter(dictiona):
    return pprint.pprint(dictiona)


class Nature:
    
    def metal(self, shape:str, metalType:str, flexibility:str, color:str):
        """  """
        metal = {
            "shape" : shape,
            "metal_type" : metalType,
            "flexibility" : flexibility,
            "color" : color
        }
        pretified = pprinter(metal)
        logger.info(f"metal with {pretified} attribute had saved")
        return metal


    def wood(self, shape, woodType, flexibility, color):
        """  """
        wood = {
            "shape" : shape,
            "wood_type" : woodType,
            "flexibility" : flexibility,
            "color" : color
        }
        pretified = pprinter(wood)
        logger.info(f"wood with {wood} attribute had saved")
        return wood

    def plastic(self, shape, plasticType, flexibility, color):
        """  """
        plastic = {                
            "shape" : shape,
            "plastic_type" : plasticType,
            "flexibility" : flexibility,
            "color" : color
        }        
        pretified = pprinter(plastic)
        logger.info(f"plastic with {plastic} attribute had saved")
        return plastic

    def glass(self, shape:str, glassType:str, flexibility:str, color:str):
        """  """
        glass = {
            "shape" : shape,
            "glass_type" : glassType,
            "flexibility" : flexibility,
            "color" : color
        }
        pretified = pprinter(glass)
        logger.info(f"glass with {glass} attribute had saved")
        return glass


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


class Pet(Living):
    """ A List of pets from cat to fishes 
    there are kinds of pets you can choose
    for seeing the list you should call Pet.animal_list()
    if you choose any cat, dog, bird or fish outside of the list
    it will raise an Error"""

    def __init__(self, cat=None, dog=None, bird=None, fish=None):
        self.cat = cat
        self.dog = dog
        self.bird = bird
        self.fish = fish

        if cat: 
            Living.animal_behaviors(cat)
            
        if dog:
            Living.animal_behaviors(dog)
        
        if fish:
            Living.animal_behaviors(fish)

    @staticmethod
    def animal_list(pet):
        """ A list of Available Cats, Dogs, Birds or fishes 
        you only can use this avalilable pets"""
        
        birds = [
                "kiwi",
                "eagle",
                "parret",
                "crow",
                "pigeon",
                "owl"]

        if pet == "bird":
            return birds
        elif pet == "cat":
            return cats
        elif pet == "dog":
            return dogs
        elif pet == "fish":
            return fihses
        else:
            raise ValueError("The Entered Pet is not added yet")

def physicality(hardship, unit, weight, area):
    physica = {
        "hardship" : hardship,
        "unti" : unit,
        "weight" : weight,
        "area" : area
    }
    pretified = pprinter(physica)
    logger.info(f"physicality with {physica} attribute had saved")
    return physica


# End