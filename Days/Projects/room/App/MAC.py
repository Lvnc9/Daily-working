#!/usr/bin/python
# Start
# MAC Module
# Modules
import logMac
import collections 


class Mac:
    """ USAGE  will get added as soon as possible """
    
    logger = logMac.LogWriter()
    class Nature:
        
        def metal(self, shape:str, metalType:str, flexibility:str, color:str):
            """  """
            metal = {
                "shape" : shape,
                "metal_type" : metalType,
                "flexibility" : flexibility,
                "color" : color
            }
            Mac.logger.info(f"metal with {metal} attribute had saved")
            return metal


        def wood(self, shape, woodType, flexibility, color):
            """  """
            wood = {
                "shape" : shape,
                "wood_type" : woodType,
                "flexibility" : flexibility,
                "color" : color
            }
            Mac.logger.info(f"wood with {wood} attribute had saved")
            return wood

        def plastic(self, shape, plasticType, flexibility, color):
            """  """
            plastic = {                
                "shape" : shape,
                "plastic_type" : plasticType,
                "flexibility" : flexibility,
                "color" : color
            }        
            Mac.logger.info(f"plastic with {plastic} attribute had saved")
            return plastic

        def glass(self, shape:str, glassType:str, flexibility:str, color:str):
            """  """
            glass = {
                "shape" : shape,
                "glass_type" : glassType,
                "flexibility" : flexibility,
                "color" : color
            }
            Mac.logger.info(f"glass with {glass} attribute had saved")
            return glass

    class Physicality:
        pass

    
    class Living():
        pass

    
lala = Mac.Nature.glass('fsd', 'gdsg', 'gds', 'gdsg', 'ggs g')
print(lala)

# End