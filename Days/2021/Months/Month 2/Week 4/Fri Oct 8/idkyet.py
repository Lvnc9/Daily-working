#! python3.9.2
# Start 
# TODO: Explaining the game
# TODO: Modules

class Contact(object):
    """**Parent of the subclass**
    work as the first parent class"""

    def __init__(self, name:str='', fname:str='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.fname = fname
    

class AddressHolder:
    def __init__(self, street='', city='', state='', code='',
    **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact, AddressHolder):
    def __init__(self, phone:str='', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone

lil = Friend('0432-424-3244')
lil.

class Big:
    class __Biger:
        def __init__(self, name):
            self.name = name
            self.id = 1
# End