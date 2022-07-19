#! python3
# Start
# Modules
import os

# The Useless version of collecting data from the neighbers
class Neighber:
    class Contact:
        """Using the basic of the inheritence
        with initilaizing new parameters"""

        def __init__(self, name, email):
            "Creating the base info of the Futre Freinds"
            self.name = name
            self.email = email

    class AddressHolder:
        """Using the basic of the inheritence
        with adding a new class to the main path of 
        the info gathering"""

        def __init__(self, streat, state, city, code):
            self.streat = streat
            self.state = state
            self.city = city
            self.code = code

    class Friend(Contact, AddressHolder):
        """Gathering and using 2 classes and 
        instancing them"""

        def __init__(self, name, email, streat, state, city, code):
            super().__init__(name, email)
            super().__init__(streat, state, city, code,)
        

# the usefull version of working data with the neighbers

class Contact:
    "Work infos"
    all_contacts = []
    
    def __init__(self, name='', email='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class AddressHolder:
    """Address info\ntaking some data about the 
    Current location"""

    def __init__(self, state='', city='', streat='', code='', **kwargs):
        super().__init__(**kwargs)
        self.state = state
        self.city = city
        self.streat = streat
        self.code = code

class Friend(Contact, AddressHolder):
    """Summation of the all datas together to give the
    Asked Output"""
    
    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone


F1 = Friend('432-423-4324')


# End