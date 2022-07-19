#! python3 
# Start
# Modules 

# Neighbers pesonal info
class Contact:
    "Gather the personal infos"
    all_contacts = []

    def __init__(self, email='', name='', **kwargs):
        super().__init__(**kwargs)
        self.email = email
        self.name = name
        self.all_contacts.append(self)
        
    def caller(self):
        if self.phone:
            return 100
# Locations info
class AddressHolder:
    "Gather address information and store it"

    def __init__(self, state='', city='', streat='', code='', **kwargs):
        super().__init__(**kwargs)
        self.state = state
        self.city = city
        self.streat = streat
        self.code = code


class Friend(Contact, AddressHolder):
    """Gather all the information of our friends and then
    initilize it again together"""

    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)
        kwargs['phone'] = phone

T1 = Friend('323-432-4324', name='pashmak', email='sam.mohammadi2154@gmail.com', city='Ohaio')
print(T1.all_contacts.remove('323-432-4324'))

# End