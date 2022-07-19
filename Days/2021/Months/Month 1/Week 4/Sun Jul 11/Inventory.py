#! python3
# Start
# An not at all complete programm for saving the items into the inventory
# Modules

class Inventory:

    def lock(self, item_type):
        """Select the type of item that is going to
        be manipulated.
        
        This method will lock theitem so nobody else can manipulate the
        inventory until it's returned.
        
        This preventsselling the same item to two different
        customers."""

        pass
    
    def unlock(self, item_type):
        '''Release the given type so that other
        customers can access it.'''
        
        pass

    def purchase(self, item_type):
        '''If the item is not locked, raise an exception.
        If the item_type does not exist, raise an exception. If the item is currently
        
        out of stock, raise an exception.
        If the item is available, subtract one item and return
        the number of items left.'''
        
        pass

item_type = 'widget'
inv = Inventory()
inv.lock(item_type)

try:
    num_left = inv.purchase(item_type)

except InvalidItemType:
    print(f"My Appolgize!\nwe dont sell {item_type}")

except OutOfStock:
    print("Sorry the item's out of stock!")

else:
    print(f"Purchase Complete. ")
# End