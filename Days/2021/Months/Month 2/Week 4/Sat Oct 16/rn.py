#! python3.9.2
# Start
### this file is about to all training and remembernece of the past informations
# TODO : Modules

class Contact(object):
    """ One of the base parent class
    Moving information from the top to the bottom """
    def __init__(self, name='', email='', phone='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.phone = phone

class AddressHolder(object):
    """ One of the base parent class
    Moving information from the top to the bottom """

    def __init__(self, street='', city='', state='', code='', **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friends(AddressHolder, Contact):
    def __init__(self, phone='', **kwargs):
        kwargs.update(dict(phone=phone))
        super().__init__(**kwargs)
        self.phone = phone
    
    def Shower(self):
        print("The Address\n", self.street, self.city,
        self.state, self.code)

address_shape = Friends( street='Sfj=4324=342', city='Sd', state='DF', code='432423')
address_shape.Shower()


# End