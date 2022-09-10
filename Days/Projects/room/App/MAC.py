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


def animal_behaviors(cat=None, dog=None, bird=None, fish=None):
    if cat:
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

    if dog:
        attrs = {
            "sleeping" : True,
            "friendly" : True,
            "sound" : True,
            "jumpping" : True,
            "barking" : True,
            "moving" : True
        }
        return attrs
    
    if bird:
        attrs = {
            "sleeping" : True,
            "friendly" : True,
            "sound" : True,
            "flying" : True,
            "talking" : True,
        }
        return attrs

    if fish:
        attrs = {
            "sleeping" : True,
            "friendly" : False,
            "jumpping" : False,
            "sound" : False,
            "swiming" : True,
            "bobbling" : True
        }
        return attrs


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


class Living():

    def __init__(self):
        self.logger = logMac.LogWriter()
        logger.file_name = "mac_loger.log"

    def pet(self, cat=None, dog=None, fish=None, bird=None):
        if cat: 
            animal_behaviors(cat)
        
        if dog:
            animal_behaviors(dog)
        
        if fish:
            animal_behaviors(fish)
        
        if bird:
            animal_behaviors(bird)

    def planet(self, small_tree=None, cactus=None, stem_planet=None):
        pass


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

example = Living.pet()
# End